# -*- coding: utf-8 -*-
import pandas as pd

from methods import vote_untour, vote_deuxtours, coombs


def read_file(file_name):
    print("-------------- Fichier : ", file_name, " ----------------------")
    global data
    data = pd.read_csv(file_name, encoding="ISO-8859-1", header=None)  # Extraction
    data.index += 1 # Pas de condidat zero
    columns = list(data.index)
    data_unique = get_occurence_classement(data, columns)

    print("-------- Les différents classement disponible -----------")
    print(data_unique)

    return data_unique, columns

def get_occurence_classement(data_set, columns):
    nbr_occur_class = []  # Liste contenant le nombre d'occurence pour chaque classement
    print("Nombre de classements distincts disponible : ", data_set.T.drop_duplicates().T.shape[1])
    data_unique = data_set.T.drop_duplicates().T  # Retourne les classement
    data_unique = data_unique.T  # Transposé les lignes et les colonnes


    for feature in data_set.T.groupby(columns).groups.values():
        data_unique.loc[feature[0], "number"] = feature.shape[0]
        nbr_occur_class.append(feature.shape[0])
    # Trie les classement selon leurs orrurences dans l'ordre décroissant
    data_unique = data_unique.sort_values(by=["number"], ascending=False)

    return data_unique



if __name__ == "__main__" :
    data_files = ["data/profil1.csv", "data/profil2.csv", "data/profil3.csv", "data/exo_1.csv", "data/exo_2.csv", "data/exo_3.csv"]
    file_data = "data/profil1.csv"
    data_unique, columns = read_file(file_data)
    print("------------------ Méthode Vote a un tours ------------------")
    vote_untour.vote_un_tour(data_unique, columns)
    print("------------------ Méthode Vote a deux tours ------------------")
    vote_deuxtours.vote_deux_tours(data_unique, columns, data)
    print("------------------ Coombs ------------------")
    coombs.coombs(data_unique, columns)





