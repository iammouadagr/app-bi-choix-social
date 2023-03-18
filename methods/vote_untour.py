# -*- coding: utf-8 -*-
import pandas as pd


def vote_un_tour(data_set, columns):
    print("---------------------- Méthode de classement avec Vote à Un tour ------------------------")
    classement = pd.DataFrame(columns=["Candidat", "Nbr_Electeurs"])
    for col in columns:
        group = data_set.groupby([col])['number'].agg('sum')  # Calculer la sommes des electeurs pour chaque candidat
        if 1 == group.index[0]:
            classement.loc[col, :] = [col, group.iloc[0]]
        else:
            classement.loc[col, :] = [col, 0]

    classement.sort_values(by=["Nbr_Electeurs"], ascending=False, inplace=True, ignore_index=True)

    print("#------------ Le classement avec la méthode à un tour  ----------------# ")
    print(classement, "\n")

    print("Le gagnant est  le candidat n°: ", classement.iloc[0]["Candidat"], " avec : ",
          classement.iloc[0]['Nbr_Electeurs'], " points\n")



