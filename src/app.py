from flask import Flask, render_template, request, jsonify
import pandas as pd
from thefuzz import process
import logging
from flask_caching import Cache

app = Flask(__name__, template_folder="../templates", static_folder="../static")

# Configuration du logging pour le debug
logging.basicConfig(level=logging.DEBUG)

# Configuration de Flask-Caching
#cache = Cache(app, config={'CACHE_TYPE': 'simple'})

# Chemin vers le fichier Excel contenant les données
EXCEL_FILE = 'Conso 2024.xlsx'

# Chargement des données depuis la sheet "Conso 2024"
try:
    df = pd.read_excel(EXCEL_FILE, sheet_name='Conso 2024')
    df.drop_duplicates(inplace=True)  # Retirer les doublons
except Exception as e:
    logging.error(f"Erreur lors du chargement du fichier Excel: {e}")
    df = pd.DataFrame()  # Créer un DataFrame vide en cas d'erreur

#@cache.memoize(timeout=300)
def get_salaries(job_title):
    """
    Récupère les salaires pour un intitulé de poste donné.
    
    Args:
        job_title (str): L'intitulé de poste pour lequel récupérer les salaires.
    
    Returns:
        tuple: Une liste des intitulés de postes corrigés et une liste de salaires.
    """
    try:
        # Liste des intitulés de postes disponibles dans les données
        choices = df['Position'].tolist()
        
        # Extraction des correspondances pour l'intitulé de poste donné dans une liste de tuples contenant l'intitulé de poste 
        # et son score de correspondance
        matches = process.extract(job_title, choices)
        
        # Filtrer les correspondances par un seuil de score raisonnable
        threshold = 60
        filtered_matches = [match for match in matches if match[1] >= threshold]
        
        # Liste des intitulés de postes corrigés
        corrected_job_titles = [match[0] for match in filtered_matches]
        salaries = []

        # Récupération des salaires pour chaque intitulé de poste corrigé
        for title in corrected_job_titles:
            filtered_df = df[df['Position'] == title]
            for index, row in filtered_df.iterrows():
                salary = row['Total Annual Salary and Bonus in €']
                country = row['Country']
                # Ajout du salaire à la liste des salaires
                salaries.append([country, round(salary, 2), 'EUR'])
        
        return corrected_job_titles, salaries
    except Exception as e:
        logging.error(f"Erreur lors de la récupération des salaires: {e}")
        return [], []

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
        corrected_job_titles, salaries = get_salaries(job_title)
        return jsonify({'corrected_job_titles': corrected_job_titles, 'salaries': salaries})
    except Exception as e:
        logging.error(f"Erreur lors de la recherche: {e}")
        return jsonify({'error': 'Error occurred while fetching data.'}), 500

if __name__ == '__main__':
    # Démarrage de l'application Flask en mode debug
    app.run(debug=True)
