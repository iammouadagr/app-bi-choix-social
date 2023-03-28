import numpy as np

def schulze(votes):
    # Calcul les duels entre chaque paire de candidats
    num_candidates = 9
    pairwise_votes = np.zeros((num_candidates, num_candidates))
    for i in range(1, num_candidates):
        for j in range(1,num_candidates):
            if i != j:
                pairwise_votes[i][j] = sum([1 for k in range(num_candidates)
                                            if votes[i][k] > votes[j][k]])

    # Calcul le chemin le plus fort entre chaque paire de candidats
    strongest_path = np.zeros((num_candidates, num_candidates))
    for i in range(1,num_candidates):
        for j in range(1,num_candidates):
            if i != j:
                if pairwise_votes[i][j] > pairwise_votes[j][i]:
                    strongest_path[i][j] = pairwise_votes[i][j]
                else:
                    strongest_path[i][j] = 0

    for i in range(1,num_candidates):
        for j in range(1,num_candidates):
            if i != j:
                for k in range(num_candidates):
                    if i != k and j != k:
                        strongest_path[j][k] = max(strongest_path[j][k],
                                                   min(strongest_path[j][i], strongest_path[i][k]))

    # Calcul de l'ensemble de Schwartz de candidats
    schwartz_set = set()
    for i in range(1,num_candidates):
        is_member = True
        for j in range(1,num_candidates):
            if i != j and strongest_path[j][i] < strongest_path[i][j]:
                is_member = False
                break
        if is_member:
            schwartz_set.add(i)

    # Calculer le beatpath pour chaque candidat dans l'ensemble de Schwartz
    beatpath_strength = np.zeros(num_candidates)
    for i in schwartz_set:
        for j in range(1,num_candidates):
            if i != j:
                beatpath_strength[i] += min(strongest_path[i][j], strongest_path[j][i])

    # Tri des candidats par force de beatpath et renvoyez le gagnant
    sorted_candidates = sorted(range(num_candidates), key=lambda x: beatpath_strength[x], reverse=True)
    print("Le gagnant est le candidat ", sorted_candidates[0])