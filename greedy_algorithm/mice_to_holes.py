# ASSIGN MICE TO HOLES

def assign_hole(mice: list, holes: list):
    if len(mice) != len(holes):
        return "Number of mice and holes not the same"

    mice.sort()
    holes.sort()

    max_diff = 0
    for i in range(len(mice)):
        if max_diff < abs(mice[i] - holes[i]):
            max_diff = abs(mice[i] - holes[i])
    return max_diff


mice = [4, -4, 2]
holes = [4, 0, 5]

min_time = assign_hole(mice, holes)
print(min_time)
