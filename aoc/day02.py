def is_safe(levels):
    asc = all(1 <= levels[i+1] - levels[i] <= 3 for i in range(len(levels) - 1))
    desc = all(1 <= levels[i] - levels[i+1] <= 3 for i in range(len(levels) - 1))
    return asc or desc

def can_be_safe(levels):
    for i in range(len(levels)):
        edited = levels[:i] + levels[i+1:]
        if is_safe(edited): 
            return True
    return False

def a():
    safe = 0
    with open("./inputs/day02.txt", "r") as file:
        for line in file:
            levels = list(map(int, line.split()))
            if is_safe(levels):
                safe += 1
    return safe

def b():
    safe = 0
    with open("./inputs/day02.txt", "r") as file:
        for line in file:
            levels = list(map(int, line.split()))
            if is_safe(levels) or can_be_safe(levels):
                safe += 1
    return safe