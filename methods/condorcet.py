# -*- coding: utf-8 -*-

import pandas as pd

from methods.copeland import copland
from methods.min_max import min_max


def condorcet(data_unique, columns, data):
    condorcet = pd.DataFrame(columns=columns)
    # Pour chaque couple calculer les duels
    for i in range(1, len(columns) + 1):
        for j in range(i + 1, len(columns) + 1):
            for_first = data_unique.loc[
                data_unique[i] < data_unique[j], "number"].agg('sum')

            # Nombre de vote total - nombre de vote pour le premier condidat
            for_second = data.shape[1] - for_first

            condorcet.loc[i, j] = for_first
            condorcet.loc[j, i] = for_second

    print("Le tableau de condorcet : ")
    print(condorcet, "\n")
    gagnant = False

    for i in range(1, len(columns) + 1):
        mask = condorcet[i] < condorcet.loc[i, :]
        if mask[mask == True].shape[0] == len(columns) - 1:
            print("Le gagnant est donc le condidat n°: ", i, "\n")
            gagnant = True
    if not gagnant:
        print("Aucun gagnant avec condorcet, donc voir avec la méthode min-max et copland\n")
        min_max(data_unique, columns, data)
        copland(data_unique, columns, data)

