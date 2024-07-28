def get_most_common_enemy(enemies_dict):
    current_max = float('-inf')
    most_enemy = None
    for enemy in enemies_dict:
        if enemies_dict[enemy] > current_max:
            most_enemy = enemy
            current_max = enemies_dict[enemy]

    return most_enemy
