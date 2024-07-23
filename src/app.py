import pandas as pd
from thefuzz import process
import logging
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder="../templates", static_folder="../static")

# Configuration du logging pour le debug
logging.basicConfig(level=logging.DEBUG)

# Chemin vers le fichier Excel contenant les données
EXCEL_FILE = 'Conso 2024.xlsx'

def load_and_clean_data(file_path):
    try:
        # Charger uniquement la feuille "Conso 2024"
        df = pd.read_excel(file_path, sheet_name='Conso 2024')
        
        # Garder seulement les colonnes spécifiées
        df = df[['Country', 'Position', 'Total Annual Salary and Bonus in €']]
        
        # Supprimer les lignes avec des valeurs manquantes
        df.dropna(inplace=True)
        
        # Retirer les doublons
        df.drop_duplicates(inplace=True)
        
        return df
    except Exception as e:
        logging.error(f"Erreur lors du chargement et du nettoyage du fichier Excel: {e}")
        return pd.DataFrame()  # Créer un DataFrame vide en cas d'erreur

# Charger et nettoyer les données
df = load_and_clean_data(EXCEL_FILE)

def get_salaries(job_title):
    """
    Récupère les salaires pour un intitulé de poste donné.
    
    Args:
        job_title (str): L'intitulé de poste pour lequel récupérer les salaires.
    
    Returns:
        dict: Un dictionnaire avec les intitulés de postes corrigés comme clés et les salaires moyens par pays comme valeurs.
    """
    try:
        # Liste des intitulés de postes disponibles dans les données
        choices = df['Position'].tolist()
        
        # Extraction des correspondances pour l'intitulé de poste donné dans une liste de tuples contenant l'intitulé de poste 
        # et son score de correspondance
        matches = process.extract(job_title, choices, limit=50)
        
        # Filtrer les correspondances par un seuil de score raisonnable
        threshold = 80
        filtered_matches = [match for match in matches if match[1] >= threshold]
        
        # Liste des intitulés de postes corrigés
        corrected_job_titles = list(set([match[0] for match in filtered_matches]))
        salary_dict = {}

        # Récupération des salaires pour chaque intitulé de poste corrigé
        for title in corrected_job_titles:
            filtered_df = df[df['Position'] == title]
            avg_salaries = filtered_df.groupby(['Country'], as_index=False)['Total Annual Salary and Bonus in €'].mean()
            avg_salaries['Total Annual Salary and Bonus in €'] = avg_salaries['Total Annual Salary and Bonus in €'].round(2)
            salary_dict[title] = avg_salaries[['Country', 'Total Annual Salary and Bonus in €']].values.tolist()
        
        return salary_dict
    except Exception as e:
        logging.error(f"Erreur lors de la récupération des salaires: {e}")
        return {}

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Route principale qui rend la page d'accueil.
    
    Returns:
        str: Le contenu HTML de la page d'accueil.
    """
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    """
    Route de recherche qui traite la soumission du formulaire et renvoie les résultats JSON.
    
    Returns:
        Response: Une réponse JSON contenant les intitulés de postes corrigés et les salaires associés.
    """
    try:
        job_title = request.form['job_title']
        salary_dict = get_salaries(job_title)
        return jsonify(salary_dict)
    except Exception as e:
        logging.error(f"Erreur lors de la recherche: {e}")
        return jsonify({'error': 'Error occurred while fetching data.'}), 500

if __name__ == '__main__':
    # Démarrage de l'application Flask en mode debug
    app.run(debug=True)
