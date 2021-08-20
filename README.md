# 810_airtable
Methodes pour requeter et filtrer des listes AirTable

- On met les parametres de connexion a airtable dans un fichier config en .json.


```
{
    "AirTable API key" : ""  , 
    "AirTable base ID" : "", 
    "AirTable table Name" : "",
    "AirTable colonne a filtrer" : "",
    "AirTable valeur a filtrer" : ""
}

```

- le module a_at_loader_810.py permet de recuperer l'ensemble des donnees de la liste. Sa methode _filter_at_pages()_ permet de filtrer sur une colonne.

On peut utiliser le fichier json pour definir la colonne sur laquelle on souhaite filtrer et la valeur associée, ou bien, on peut mettre ces elements en dur dans le code.

Le fichier .ipynb sert d'exemple d'utilisation.
