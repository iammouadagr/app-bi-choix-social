# -*- coding: utf-8 -*-

import pandas as pd

def min_max(condorcet, columns):
    print("--------------------- Min Max --------------------")
    print("Minimax sélectionne comme vainqueur le candidat dont la plus grande défaite par paire est "
          "inférieure à la plus grande défaite par paire de tout autre candidat \n")

    classement = pd.DataFrame(data={"condidat": columns, "points": condorcet.max(axis=0).values})
    classement.sort_values(by=["points"], ascending=True, inplace=True, ignore_index=True)

    print("Le classement avec la méthode min_max : ")
    print(classement, "\n")

    if classement.iloc[0]["points"] == classement.iloc[1]["points"]:
        print("Cas d'égalité pour MinMax, donc aucun condidat ne gagne pour MinMax")
    else:
        print("Le gagnant avec la méthode min-max est donc le condidat n°: ", classement.iloc[0]["condidat"]
              , " avec : ", classement.iloc[0]['points'], " points de la plus grosse perte\n")

