# 810_airtable
Methodes pour requeter et filtrer des listes [AirTable](https://airtable.com/)

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

- le module [a_at_loader_810.py](https://github.com/MaximoRose/810_airtable/blob/main/a_at_loader_810.py) permet de recuperer l'ensemble des donnees de la liste. Sa methode _filter_at_pages()_ permet de filtrer sur une colonne.
- le module [a_load_paramz_810.py](https://github.com/MaximoRose/810_airtable/blob/main/a_load_paramz_810.py) permet de recuperer l'ensemble des paramètres du fichiers .json sous la forme d'attribut d'un objet _api_parameters()_. 

On peut utiliser le fichier json pour definir la colonne sur laquelle on souhaite filtrer et la valeur associée, ou bien, on peut mettre ces elements en dur dans le code.

Le fichier [airtable_tst.ipynb](https://github.com/MaximoRose/810_airtable/blob/main/airtable_tst.ipynb) sert d'exemple d'utilisation.

On se sert de ces modules pour charger les éléments à requêter pour nos analyses YouTube. C'est par exemple ainsi qu'on avait défini la liste de chaîne YouTube que nous souhaitions requêter pour [notre analyse de la performance des chaînes YouTube des institutions culturelles françaises](https://github.com/MaximoRose/OS_YouTube_Consultant) : un code s'appuyait sur une liste de chaîne définit dans AirTable qu'on allait ensuite requêter par un script python qui permettait de générer des fichiers .json issus des données renvoyées par les API YouTube. Un fichier Jupyter NoteBook servait ensuite à l'analyse de ces données.
