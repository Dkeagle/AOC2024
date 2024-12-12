import itertools

def is_ordered(update, rules):
    unordered = 0
    for rule in rules:
        if rule[0] in update and rule[1] in update and update.index(rule[1]) < update.index(rule[0]):
            unordered += 1
    return False if unordered > 0 else True

def find_middle(lst):
    return lst[len(lst) // 2]

def find_ordered(update, rules):
    for perm in list(itertools.permutations(update)):
        if is_ordered(perm, rules):
            return perm

def a():
    input = []
    total = 0
    with open("./inputs/day05.txt", "r") as file:
        for line in file: 
            input.append(line.strip())
    split = input.index('')
    rules, updates = input[:split], input[split+1:]
    rules = [tuple(rule.split("|")) for rule in rules]
    updates = [update.split(",") for update in updates]
    for update in updates:
        if is_ordered(update, rules): total += int(find_middle(update))
    return total

def b():
    input = []
    total = 0
    with open("./inputs/day05.txt", "r") as file:
        for line in file:
            input.append(line.strip())
    split = input.index('')
    rules, updates = input[:split], input[split+1:]
    rules = [tuple(rule.split("|")) for rule in rules]
    updates = [update.split(",") for update in updates]
    cpt = 0
    for update in updates:
        if not is_ordered(update, rules): 
            total += int(find_middle(find_ordered(update, rules)))
        cpt += 1
        print(f"{update} done.\n{cpt}/{len(updates)} => {cpt/len(updates)*100:.2f}%")
    return total
