def calculate_elo(rating1, rating2, result):
    """
    Calculate the new ELO rating for two concepts
    :param rating1: ELO rating of concept 1
    :param rating2: ELO rating of concept 2
    :param result: Result of the comparison (1 if concept 1 wins, 0 if concept 2 wins)
    :return: The new ELO ratings for concept 1 and concept 2
    """
    K = 32
    expected1 = 1 / (1 + 10 ** ((rating2 - rating1) / 400))
    expected2 = 1 / (1 + 10 ** ((rating1 - rating2) / 400))
    new_rating1 = rating1 + K * (result - expected1)
    new_rating2 = rating2 + K * ((1 - result) - expected2)
    return new_rating1, new_rating2