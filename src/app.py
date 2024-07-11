from flask import Flask, render_template, request, jsonify
import pandas as pd
from thefuzz import process
from currency_converter import CurrencyConverter

app = Flask(__name__, template_folder="../templates", static_folder="../static")

# Chemin vers le fichier Excel contenant les données
EXCEL_FILE = '../excelBE.xlsx'

# Chargement des données depuis le fichier Excel
df = pd.read_excel(EXCEL_FILE)

# Initialisation du convertisseur de devises
c = CurrencyConverter()

def get_salaries(job_title):
    """
    Récupère les salaires pour un intitulé de poste donné.
    
    Args:
        job_title (str): L'intitulé de poste pour lequel récupérer les salaires.
    
    Returns:
        tuple: Une liste des intitulés de postes corrigés et une liste de salaires convertis en EUR.
    """
    # Liste des intitulés de postes disponibles dans les données
    choices = df['job title'].tolist()
    
    # Extraction des correspondances pour l'intitulé de poste donné dans une liste de tuples contenant l'intitulé de poste 
    # et son score de correspondance
    matches = process.extract(job_title, choices)
    
    # Filtrer les correspondances par un seuil de score raisonnable
    threshold = 60
    filtered_matches = [match for match in matches if match[1] >= threshold]
    
    # Liste des intitulés de postes corrigés
    corrected_job_titles = [match[0] for match in filtered_matches]
    salaries = []

    # Récupération et conversion des salaires pour chaque intitulé de poste corrigé
    for title in corrected_job_titles:
        filtered_df = df[df['job title'] == title]
        for index, row in filtered_df.iterrows():
            salary = row['salary']
            currency = row['currency']
            # Conversion du salaire en EUR si nécessaire
            if currency != 'EUR':
                salary = c.convert(salary, currency, 'EUR')
            # Ajout du salaire converti à la liste des salaires
            salaries.append([row['country'], round(salary, 2), 'EUR'])
    
    return corrected_job_titles, salaries

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
    job_title = request.form['job_title']
    corrected_job_titles, salaries = get_salaries(job_title)
    return jsonify({'corrected_job_titles': corrected_job_titles, 'salaries': salaries})

if __name__ == '__main__':
    # Démarrage de l'application Flask en mode debug
    app.run(debug=True)
