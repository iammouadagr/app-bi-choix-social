from collections import defaultdict

def ranked_pairs(votes):
    """
      Algorithme des paires classées sur la liste de votes donnée.

        Parameters:
            votes (list[list[int]]) : une liste de votes de préférence, où chaque vote est une liste d'entiers représentant
                l'ordre dans lequel les alternatives sont préférées.

        """
    # Create a dictionary to store the pairwise comparisons
    pairwise_comparisons = defaultdict(int)
    for vote in votes:
        for i, candidate1 in enumerate(vote):
            for candidate2 in vote[i+1:]:
                pairwise_comparisons[(candidate1, candidate2)] += 1

    # Sort the pairwise comparisons in decreasing order of strength
    sorted_comparisons = sorted(pairwise_comparisons.items(), key=lambda x: -x[1])

    # Create a dictionary to keep track of which candidates have already been added to the final order
    included_candidates = {}

    # Iterate over the sorted pairwise comparisons and add each candidate to the final order if it does not create a cycle
    for comparison in sorted_comparisons:
        candidate1, candidate2 = comparison[0]
        if candidate1 not in included_candidates or candidate2 not in included_candidates:
            if candidate1 not in included_candidates:
                included_candidates[candidate1] = True
            if candidate2 not in included_candidates:
                included_candidates[candidate2] = True

            # Check if adding the candidate creates a cycle
            if not creates_cycle(included_candidates.keys(), pairwise_comparisons):
                continue

            # If adding the candidate does not create a cycle, add it to the final order
            if pairwise_comparisons[(candidate1, candidate2)] > pairwise_comparisons[(candidate2, candidate1)]:
                yield candidate1
            else:
                yield candidate2

def creates_cycle(candidates, pairwise_comparisons):
    """Checks if adding any candidate to the given list of candidates creates a cycle."""
    for candidate in candidates:
        for other_candidate in candidates:
            if candidate == other_candidate:
                continue
            if (candidate, other_candidate) in pairwise_comparisons and (other_candidate, candidate) in pairwise_comparisons:
                if pairwise_comparisons[(candidate, other_candidate)] > pairwise_comparisons[(other_candidate, candidate)]:
                    return True
    return False
