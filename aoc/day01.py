def a():
    left, right = [], []
    distance = 0

    with open("./inputs/day01.txt", "r") as file:
        for line in file:
            l, r = map(int, line.split())
            left.append(l)
            right.append(r)
    
    while left:
        distance += abs(min(left)-min(right))
        left.remove(min(left))
        right.remove(min(right))

    return distance

def b():
    left, right = [], []
    similarity = 0

    with open("./inputs/day01.txt", "r") as file:
        for line in file:
            l, r = map(int, line.split())
            left.append(l)
            right.append(r)

    for i in left:
        similarity += i * right.count(i)

    return similarity