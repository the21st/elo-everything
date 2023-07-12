def calculate_elo(rank1, rank2, outcome):
    """
    Calculate the new ELO ranking for two concepts.
    :param rank1: The current ELO ranking of concept 1.
    :param rank2: The current ELO ranking of concept 2.
    :param outcome: The outcome of the comparison (1 if concept 1 is chosen, 0 if concept 2 is chosen).
    :return: The new ELO rankings for concept 1 and concept 2.
    """
    k = 32
    expected_outcome1 = 1 / (1 + 10 ** ((rank2 - rank1) / 400))
    expected_outcome2 = 1 - expected_outcome1

    new_rank1 = rank1 + k * (outcome - expected_outcome1)
    new_rank2 = rank2 + k * ((1 - outcome) - expected_outcome2)

    return new_rank1, new_rank2