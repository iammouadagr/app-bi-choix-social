# -*- coding: utf-8 -*-
import pandas as pd

def vote_deux_tours(data_unique, columns, data):
    classement = pd.DataFrame(columns=["Condidat", "Nbr_Electeurs"])
    for col in columns:
        group = data_unique.groupby([col])['number'].agg('sum')
        if 1 == group.index[0]:
            classement.loc[col, :] = [col, group.iloc[0]]
        else:
            classement.loc[col, :] = [col, 0]

    classement.sort_values(by=["Nbr_Electeurs"], ascending=False, inplace=True, ignore_index=True)
    # Récuperer les deux premiers candidats ayant le plus de voix au premier tour
    condidat_frst = classement.iloc[0]['Condidat']
    condidat_snd = classement.iloc[1]["Condidat"]

    # Calculer le nombre de voix du premier candidat
    for_first = data_unique.loc[
        data_unique[condidat_frst] < data_unique[condidat_snd], "number"].agg(
        'sum')
    # Calculer mle nombre de voix du deuxieme candidat
    for_second = data.shape[1] - for_first  # Nombre de vote total - nombre de vote pour le premier condidat

    print("#------------ Le classement avec la méthode à deux tours  ----------------#")
    if for_first > for_second:
        print("Le gagnant est le condidat n°: ", condidat_frst, " avec : ", for_first, " le deuxième est donc"
                                                                                             " le condidat n°",
              condidat_snd, " avec : ", for_second, "\n")
    else:
        print("Le gagnant est donc le condidat n°: ", condidat_snd, " avec : ", for_second, "le deuxième est "
                                                                                               "donc le condidat n",
              condidat_frst, " avec : ", for_first, "\n")