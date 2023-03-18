# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

from methods.vote_untour import vote_un_tour
from methods.vote_deuxtours import vote_deux_tours
from methods.coombs import coombs
from methods.condorcet import condorcet
from methods.alternative import alternative_vote
from methods.borda import borda_vote


def read_file(file_name):
    print("-------------- Fichier : ", file_name, " ----------------------")
    global data
    data = pd.read_csv(file_name, encoding="ISO-8859-1", header=None)  # Extraction
    data.index += 1 # Pas de condidat zero
    columns = list(data.index)
    data_unique = get_occurence_classement(data, columns)

    print("-------- Les différents classement disponible -----------")
    print(data_unique)

    return data_unique, columns,data


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


def get_occurence_order_v2(data):
    standings = np.zeros((len(data.columns), len(data)))
    current_rank = np.zeros(len(data))
    votes_by_rank = []
    prev_rank = np.zeros(len(data))
    for i in range(0, len(data.columns)):  # pour chaque colonne
        for j in range(1, len(data) + 1):  # pour chaque ligne
            current_rank[j - 1] = data.iloc[:, i][j]  # on récupère la valeur
        if (np.array_equal(current_rank, prev_rank) == False):
            standings[i] = current_rank
            votes_by_rank.append(1)
            for j in range(len(data)):  # pour chaque ligne
                prev_rank[j] = current_rank[j]
        else:
            votes_by_rank[-1] += 1
            for j in range(len(data)):  # pour chaque ligne
                prev_rank[j] = current_rank[j]
    standings = standings[~(standings[:, 1] == 0)]
    return standings, votes_by_rank


if __name__ == "__main__" :
    data_files = ["profiles/profil1.csv", "profiles/profil2.csv", "profiles/profil3.csv"]
    file_data = data_files[0]
    data_unique, columns,data = read_file(file_data)

    print("------------------ Méthode Vote a un tours ------------------")
    vote_un_tour(data_unique, columns)
    print("------------------ Méthode Vote a deux tours ------------------")
    vote_deux_tours(data_unique, columns, data)
    print("------------------ Coombs ------------------")
    coombs(data_unique, columns)
    print("------------------- condorcet ---------------------")
    condorcet(data_unique, columns, data)
    print("------------------ Méthode Vote Alternative ------------------")
    standings, votes_by_rank = get_occurence_order_v2(data)
    alternative_vote(data, standings, votes_by_rank)
    print("------------------ Méthode Vote Borda ------------------")
    standings, nb_votes_par_ordre = get_occurence_order_v2(data)
    borda_vote(data, standings, votes_by_rank)






