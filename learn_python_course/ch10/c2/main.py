def merge(dict1, dict2):
    return {**dict1, **dict2}


def total_score(score_dict):
    total = 0
    for score in score_dict:
        total += score_dict[score]
    return total
