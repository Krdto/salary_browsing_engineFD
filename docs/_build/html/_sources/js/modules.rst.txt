JavaScript Documentation
========================

Functions
---------

.. js:function:: $(document).ready(function()


 * Initialise la fonction lorsque la page est prête.
 * Attache un événement d'entrée au champ de saisie du titre de poste (#job_title).

.. js:function:: $('#job_title').on('input', function()

   Evénement déclenché de=ès qu'il y à un input dans le champ #job_title.
   Effectue une requête AJAX pour chercher les postes et salaires associés.

   * Fonction de succès appelée lors de la réception de la réponse du serveur.
   * @param {Object} data - Les données renvoyées par le serveur.
   * @param {Array} data.corrected_job_titles - Liste des titres de postes corrigés.
   * @param {Array} data.salaries - Liste des salaires associés aux titres de postes.

script.js
---------

.. literalinclude:: ../../static/js/script.js
   :language: javascript
