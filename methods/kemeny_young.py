import itertools
import numpy as np

def kemeny_young(votes):
    """
    Calculer le classement Kemeny-Young d'une liste de votes de préférence.

    Parameters:
        votes (list[list[int]]) : une liste de votes de préférence, où chaque vote est une liste d'entiers représentant
            l'ordre dans lequel les alternatives sont préférées.

    """

    # Déterminer l'ensemble des alternatives
    alternatives = set(itertools.chain(*votes))

    # Calculer la matrice de préférence
    preference_matrix = {}
    for alt1 in alternatives:
        preference_matrix[alt1] = {}
        for alt2 in alternatives:
            preference_matrix[alt1][alt2] = 0
    for vote in votes:
        for i, alt1 in enumerate(vote):
            for alt2 in vote[i+1:]:
                preference_matrix[alt1][alt2] += 1

    # Calculer le classement Kemeny-Young
    min_score = float("inf")
    min_ranking = None
    for ranking in itertools.permutations(alternatives):
        score = sum(preference_matrix[ranking[i]][ranking[j]] for i in range(len(ranking)) for j in range(i+1, len(ranking)))
        if score < min_score:
            min_score = score
            min_ranking = ranking
    results = list(min_ranking)
    print("Le gagnant est le candidat ", int(results[0]))



