import re

def a():
    total = 0
    with open("./inputs/day03.txt", "r") as file:
        data = file.read()
    
    found = re.findall(r"mul\((\d{1,3}\,\d{1,3})\)", data)

    for couple in found:
        a, b = map(int, couple.split(","))
        total += a * b
    return total

def b():
    total = 0
    with open("./inputs/day03.txt", "r") as file:
        data = file.read()

    donts = re.findall(r"(don't\(\).*?)(?=do\(\)|don't\(\)|$)", data, re.DOTALL)
    for dont in donts:
        data = data.replace(dont, "")

    found = re.findall(r"mul\((\d{1,3}\,\d{1,3})\)", data)

    for couple in found:
        a, b = map(int, couple.split(","))
        total += a * b
    return total