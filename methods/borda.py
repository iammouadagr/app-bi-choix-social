import pandas as pd
import numpy as np

def borda_vote(data,standings,votes_by_rank):
    """
          Algorithme de la méthode Borda.

            Parameters:
                votes (list[list[int]]) : une liste de votes de préférence, où chaque vote est une liste d'entiers représentant
                    l'ordre dans lequel les alternatives sont préférées.

            """

    matrice=np.zeros((len(data),len(data)))
    for i in range(len(standings)): #pour chaque ordre de vote
        for j in range(len(standings[i])): #pour chaque candidat
            for k in range(j+1,len(standings[i])): #pour chaque candidat, on compare avec les candidats qui suivent
                matrice[int(standings[i][j])-1][int(standings[i][k])-1]+=votes_by_rank[i] #on ajoute le nombre de votes de l'ordre de vote à la case correspondante dans la matrice
    nb_duels_gagnes=np.zeros(len(data))
    for i in range(len(matrice)): #pour chaque candidat
        for j in range(len(matrice[i])): #pour chaque candidat
            if matrice[i][j]>matrice[j][i]: #si le candidat i a gagné plus de duels que le candidat j
                nb_duels_gagnes[i]+=1 #on ajoute 1 au nombre de duels gagnés par le candidat i

        nb_points_par_candidat=np.zeros(len(data))
        for i in range(len(matrice)):
            for j in range(len(matrice[i])):
                nb_points_par_candidat[i]+=matrice[i][j]
        gagnant=0
        max_points=0
        for i in range(len(nb_points_par_candidat)):
            if nb_points_par_candidat[i]>max_points:
                max_points=nb_points_par_candidat[i]
                gagnant=i+1
    print("Le gagnant est le candidat ", gagnant, " avec ", int(max_points), " points")
    print(nb_points_par_candidat)


