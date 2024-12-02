def a():
    safe = 0
    with open("./inputs/day02.txt", "r") as file:
        for line in file:
            levels = line.split()
            print(levels)
            for i in range(len(levels) - 1):
                current, next = int(levels[i]), int(levels[i+1])
            safe += 1
    return safe

def b():
    return