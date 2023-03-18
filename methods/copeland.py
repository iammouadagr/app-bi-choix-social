# -*- coding: utf-8 -*-

import pandas as pd

def copland(condorcet, columns):
    print("--------------------- Copland --------------------")
    print("Copland calcule pour chaque condidat le nombre de pair gagné - le nombre de pair perdu et "
          "choisi le meilleur score \n")

    classement = pd.DataFrame(columns=["condidat", "points"], data={"condidat": columns})

    for i in range(1, len(columns) + 1):
        mask = condorcet[i] < condorcet.loc[i, :]
        classement.loc[i - 1, "points"] = mask[mask == True].shape[0] - (mask[mask == False].shape[0] - 1)

    classement.sort_values(by=["points"], ascending=False, inplace=True, ignore_index=True)

    print("Le classement avec la méthode Copland : ")
    print(classement, "\n")

    if classement.iloc[0]["points"] == classement.iloc[1]["points"]:
        print("Cas d'égalité pour Copland, donc aucun condidat ne gagne pour Copland")
    else:
        print("Le gagnant avec la méthode copland est donc le condidat n°: ", classement.iloc[0]["condidat"]
              , " avec : ", classement.iloc[0]['points'], " points\n")