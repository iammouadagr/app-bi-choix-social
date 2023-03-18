import pandas as pd
import numpy as np


def alternative_vote(data,standings,votes_by_rank):
    eliminated_candidats = []

    first_place_per_candidat = np.zeros(len(data))  # on initialise le nombre de 1er votes par candidat à 0
    for i in range(len(first_place_per_candidat)):  # pour chaque candidat
        for j in range(len(standings)):  # pour chaque ordre de vote
            if standings[j][0] == i + 1:  # si le candidat est en 1ère place
                first_place_per_candidat[i] += votes_by_rank[
                    j]  # on ajoute le nombre de votes de l'ordre de vote à son nombre de 1er votes

    while (len(eliminated_candidats) <= len(data) - 3):  # tant qu'il reste plus de 2 candidats
        min_first_place = 1000000  # on initialise le nombre de 1er votes minimum à un nombre très grand
        for i in range(len(first_place_per_candidat)):  # pour chaque candidat
            if first_place_per_candidat[
                i] < min_first_place and i + 1 not in eliminated_candidats:  # si le nombre de 1er votes du candidat est inférieur au nombre de 1er votes minimum et que le candidat n'a pas déjà été éliminé
                min_first_place = first_place_per_candidat[i]  # on met à jour le nombre de 1er votes minimum
        eliminated_candidat = np.where(first_place_per_candidat == min_first_place)[0][
                               0] + 1  # on récupère le candidat éliminé, c'est celui qui a le moins de 1er votes
        eliminated_candidats.append(eliminated_candidat)
        first_place_per_candidat[eliminated_candidat - 1] = -1
        for i in range(len(first_place_per_candidat)):
            if first_place_per_candidat[i] != -1:
                first_place_per_candidat[i] = 0
        for i in range(len(standings)):
            for j in range(len(standings[i])):
                if int(standings[i][j]) not in eliminated_candidats:
                    first_place_per_candidat[int(standings[i][j]) - 1] += votes_by_rank[i]
                    break
    maxVotes = 0
    gagnant = 0
    for i in range(len(first_place_per_candidat)):
        if first_place_per_candidat[i] > maxVotes:
            maxVotes = first_place_per_candidat[i]
            gagnant = i + 1
    print("Le gagnant est le candidat ", gagnant, " avec ", int(maxVotes), " votes")


