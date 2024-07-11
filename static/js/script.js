/**
 * Initialise la fonction lorsque la page est prête.
 * Attache un événement d'entrée au champ de saisie du titre de poste (#job_title).
 */
$(document).ready(function() {
    /**
     * Événement déclenché lors de la saisie dans le champ #job_title.
     * Effectue une requête AJAX pour rechercher des titres de poste et leurs salaires associés.
     */
    $('#job_title').on('input', function() {
        var jobTitle = $(this).val();
        // Vérifie si la longueur du titre est supérieure à 1 caractère
        if (jobTitle.length > 1) {
            $.ajax({
                url: '/search', // URL de recherche
                method: 'POST', // Méthode de la requête
                data: { job_title: jobTitle }, // Données envoyées
                /**
                 * Fonction de succès appelée lors de la réception de la réponse du serveur.
                 * @param {Object} data - Les données renvoyées par le serveur.
                 * @param {Array} data.corrected_job_titles - Liste des titres de postes corrigés.
                 * @param {Array} data.salaries - Liste des salaires associés aux titres de postes.
                 */
                success: function(data) {
                    var resultsDiv = $('#results');
                    resultsDiv.empty(); // Vide les résultats précédents

                    // Regroupage des résultats par poste
                    var groupedResults = {};
                    data.corrected_job_titles.forEach(function(title, index) {
                        if (!groupedResults[title]) {
                            groupedResults[title] = [];
                        }
                        groupedResults[title].push(data.salaries[index]);
                    });

                    // Affichage des résultats regroupés
                    Object.keys(groupedResults).forEach(function(title) {
                        var jobResults = groupedResults[title];
                        var container = $('<div class="job-results"></div>');
                        container.append('<h4>Results for ' + title + ':</h4>');
                        jobResults.forEach(function(item) {
                            container.append(
                                '<div class="result-item"><p><strong>' + item[0] + '</strong> - ' + item[1] + ' ' + item[2] + '</p></div>'
                            );
                        });
                        resultsDiv.append(container);
                    });

                    // Si aucun résultat n'est trouvé
                    if (Object.keys(groupedResults).length === 0) {
                        resultsDiv.append(
                            '<div class="alert alert-warning">No data found for the given job title.</div>'
                        );
                    }
                },
                /**
                 * Fonction appelée en cas d'erreur lors de la requête AJAX.
                 */
                error: function() {
                    var resultsDiv = $('#results');
                    resultsDiv.empty();
                    resultsDiv.append('<div class="alert alert-danger">Error occurred while fetching data.</div>');
                }
            });
        } else {
            $('#results').empty(); // Vide les résultats si le titre est trop court
        }
    });
});
