# -*- coding: utf-8 -*-
import pandas as pd

def coombs(data_unique, columns):
    data = data_unique.copy()
    classement = None
    columns = columns.copy()

    while len(columns) != 1:
        classement = pd.DataFrame(columns=["condidat", "points"])

        for col in columns:
            group = data.groupby([col])['number'].agg('sum')
            # Il faut qu'il soit dernier de la liste au moins une fois
            if len(columns) == group.index[-1]:
                classement.loc[col, :] = [col, group.iloc[-1]]

        classement.sort_values(by=["points"], ascending=False, inplace=True, ignore_index=True)
        print("classement : \n", classement, " \n")
        data[data[columns].apply(lambda row: row > row[classement.iloc[0]["condidat"]], axis=1)] -= 1

        last_value = classement.iloc[0]["points"]
        print("le candidat ", classement.iloc[0]["condidat"], "est eliminé")
        columns.remove(classement.iloc[0]["condidat"])

        for i in range(1, classement.shape[0]):
            if last_value == classement.iloc[i]["points"]:
                data[data[columns].apply(lambda row: row > row[classement.iloc[i]["condidat"]], axis=1)] -= 1
                columns.remove(classement.iloc[i]["condidat"])
            else:
                break

    if len(columns) == 0:
        print("Cas d'égalité, la méthode coombs ne propose pas de classement par rapport à ce cas")
    else:
        print("Le gagnant est donc le condidat n°: ", classement.iloc[-1]["condidat"], "\n")
