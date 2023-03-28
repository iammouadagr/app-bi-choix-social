import itertools

def kemeny_young(votes):
    """
    Compute the Kemeny-Young ranking of a list of preference votes.

    Parameters:
        votes (list[list[int]]): A list of preference votes, where each vote is a list of integers representing
            the order in which the alternatives are preferred.

    Returns:
        list[int]: The Kemeny-Young ranking, represented as a list of integers, where the i-th integer represents
            the i-th alternative in the ranking.
    """

    # Determine the set of alternatives
    alternatives = set(itertools.chain(*votes))

    # Compute the preference matrix
    preference_matrix = {}
    for alt1 in alternatives:
        preference_matrix[alt1] = {}
        for alt2 in alternatives:
            preference_matrix[alt1][alt2] = 0
    for vote in votes:
        for i, alt1 in enumerate(vote):
            for alt2 in vote[i+1:]:
                preference_matrix[alt1][alt2] += 1

    # Compute the Kemeny-Young ranking
    min_score = float("inf")
    min_ranking = None
    for ranking in itertools.permutations(alternatives):
        score = sum(preference_matrix[ranking[i]][ranking[j]] for i in range(len(ranking)) for j in range(i+1, len(ranking)))
        if score < min_score:
            min_score = score
            min_ranking = ranking
    results = list(min_ranking)
    print("Le gagnant est le candidat ", int(results[0]))
    return results