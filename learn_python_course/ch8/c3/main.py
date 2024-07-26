def calculate_experience_points(level):
    xp = 0
    for i in range(1, level):
        xp += i * 5
        print(i)
    return xp


print(calculate_experience_points(4))
