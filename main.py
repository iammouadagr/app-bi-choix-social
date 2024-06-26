# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

from methods.vote_untour import vote_un_tour
from methods.vote_deuxtours import vote_deux_tours
from methods.coombs import coombs
from methods.condorcet import condorcet
from methods.alternative import alternative_vote
from methods.borda import borda_vote
from methods.schulze import schulze
from methods.kemeny_young import kemeny_young
from methods.ranked_pairs import ranked_pairs
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
    for i in range(0, len(data.columns)):
        for j in range(1, len(data) + 1):
            current_rank[j - 1] = data.iloc[:, i][j]
        if (np.array_equal(current_rank, prev_rank) == False):
            standings[i] = current_rank
            votes_by_rank.append(1)
            for j in range(len(data)):
                prev_rank[j] = current_rank[j]
        else:
            votes_by_rank[-1] += 1
            for j in range(len(data)):
                prev_rank[j] = current_rank[j]
    standings = standings[~(standings[:, 1] == 0)]
    standings_list = standings.astype(int).tolist()
    standings_list = [row for row in standings_list if any(row)]
    return standings_list, votes_by_rank


if __name__ == "__main__" :
    data_files = ["profiles/profil1.csv", "profiles/profil2.csv", "profiles/profil3.csv"]
    # Choisisez le profil souhaité 0,1,2
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
    votes, votes_by_rank = get_occurence_order_v2(data)
    alternative_vote(data, votes, votes_by_rank)
    print("------------------ Méthode Vote Borda ------------------")
    votes, votes_by_rank = get_occurence_order_v2(data)
    borda_vote(data, votes, votes_by_rank)
    print("------------------ Méthode Schulze ------------------")
    votes, nb_votes_par_ordre = get_occurence_order_v2(data)
    schulze(votes)
    print("------------------ Méthode Kemeny young ------------------")
    votes, votes_by_rank = get_occurence_order_v2(data)
    # A ne pas utiliser sauf pour le profil ayant moins de candidat (profil 1) vu la complexité du temps.
    kemeny_young(votes)
    print("------------------ Méthode Condorcet avec rangement des paires par ordre décroissant ------------------")
    for candidate in ranked_pairs(votes):
        print(candidate)



