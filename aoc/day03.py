import re

def a():
    total = 0
    with open("./inputs/day03.txt", "r") as file:
        data = file.read()
        found = re.findall(r"mul\((\d{1,3}\,\d{1,3})\)", data)

    for couple in found:
        a, b = couple.split(",")
        total += int(a) * int(b)
    return total

def b():
    total = 0
    with open("./inputs/day03.txt", "r") as file:
        data = file.read()

    print(f"{data}\n")
    donts = re.findall(r"(don't\(\).*?)(?=do\(\)|don't\(\))", data)
    for dont in donts:
        print(f"{dont}\n")
        data = data.replace(dont, "")
    print(f"{data}\n")
        
    found = re.findall(r"mul\((\d{1,3}\,\d{1,3})\)", data)
    for couple in found:
        a, b = couple.split(",")
        total += int(a) * int(b)
    return total