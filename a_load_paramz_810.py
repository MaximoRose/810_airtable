import json


class api_parameters :

    # Initialise mes parametres preferes contenu dans le fichier de config .json
    def __init__(self, nom_fichier = "./config/airtable_paramz.json"):
        # On charge le fichier json en memoire
        json_settings = self.get_paramfile(nom_fichier)
        
        # Le fichier de config doit au moins contenir la cle de l'API
        try :
            self.airtable_api_key = json_settings["AirTable API key"]
        except KeyError :
            print("Impossible de trouver la clé API AirTable")
            self.airtable_api_key = ""

        # L'ID de la base
        try :
            self.airtable_base_id = json_settings["AirTable base ID"]
        except KeyError :
            print("Impossible de trouver l'ID de la base AirTable")
            self.airtable_base_id = ""

        # Le nom de la table
        try :
            self.airtable_table_name = json_settings["AirTable table Name"]
        except KeyError :
            print("Impossible de trouver le nom de la table AirTable")
            self.airtable_table_name = ""

        # Nom de la colonne Airtable sur laquelle on souhaite filtrer
        try :
            self.airtable_filtered_colonne = json_settings["AirTable colonne a filtrer"]
        except KeyError :
            print("Impossible de trouver le nom de la colonne a filtrer dans la table AirTable")
            self.airtable_filtered_colonne = ""

        # Valeur de la colonne Airtable sur laquelle on souhaite filtrer
        try :
            self.airtable_filtered_value = json_settings["AirTable valeur a filtrer"]
        except KeyError :
            print("Impossible de trouver la valeur de la colonne a filtrer dans la table AirTable")
            self.airtable_filtered_value = ""


    # Recupere les parametres graphiques du fichier de config sous la forme d'un dictionnaire
    def get_paramfile(self, config_file = "/config/airtable_paramz.json") :
        # read file
        with open(config_file, 'r') as myfile:
            data=myfile.read()
        # parse file
        obj = json.loads(data)
        return obj