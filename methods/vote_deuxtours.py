# -*- coding: utf-8 -*-
import pandas as pd

def vote_deux_tours(data_unique, columns, data):
    print("---------------------- Deux tours ------------------------")
    classement = pd.DataFrame(columns=["condidat", "points"])

    for col in columns:
        group = data_unique.groupby([col])['number'].agg('sum')
        if 1 == group.index[0]:
            classement.loc[col, :] = [col, group.iloc[0]]
        else:
            classement.loc[col, :] = [col, 0]

    classement.sort_values(by=["points"], ascending=False, inplace=True, ignore_index=True)

    first_condidat = classement.iloc[0]['condidat']  # Condidat ayant la première place durant le premier tour
    second_condidat = classement.iloc[1]["condidat"]  # Condidat ayant la deuxième place durant le premier tour

    # Nombre de vote pour le premier condidat
    for_first = data_unique.loc[
        data_unique[first_condidat] < data_unique[second_condidat], "number"].agg(
        'sum')

    # Nombre de vote pour le deuxième condidat
    for_second = data.shape[1] - for_first  # Nombre de vote total - nombre de vote pour le premier condidat

    print("Le classement avec la méthode à deux tours : ")
    if for_first > for_second:
        print("Le gagnant est donc le condidat n°: ", first_condidat, " avec : ", for_first, " le deuxième est donc"
                                                                                             " le condidat n°",
              second_condidat, " avec : ", for_second, "\n")
    else:
        print("Le gagnant est donc le condidat n°: ", second_condidat, " avec : ", for_second, "le deuxième est "
                                                                                               "donc le condidat n",
              first_condidat, " avec : ", for_first, "\n")