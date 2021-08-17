# 810_airtable
Methodes pour requeter et filtrer des listes AirTable

- On met les parametres de connexion a airtable dans un fichier config en .json.

{
    "AirTable API key" : ""  , 
    "AirTable base ID" : "", 
    "AirTable table Name" : "",
    "AirTable colonne a filtrer" : "",
    "AirTable valeur a filtrer" : ""
}

- le module _810_airtable_ permet de recuperer l'ensemble des donnees de la liste. Sa methode, filter_at_pages(self, colonne_name = "", colonne_value = ""), permet de ne recuperer que les elements qu'on souhaite.

On peut utiliser le fichier json pour definir la colonne qu'on souhaite filtrer et la valeur associee, ou bien, on peut mettre ces elements en dur dans le code.

Le fichier .ipynb sert d'exemple d'utilisation
