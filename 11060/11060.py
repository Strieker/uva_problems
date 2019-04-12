import sys
import itertools
from collections import OrderedDict

case_number = 0

while True:
    case_number += 1
    num_of_drinks = sys.stdin.readline()
    if num_of_drinks == "":
        break
    else:
        num_of_drinks = int(num_of_drinks)
    relationships_of_drinks = OrderedDict()
    drink = ""
    relation1 = ""
    relation2 = ""
    drink_list = "Dilbert should drink beverages in this order: "
    for i in range(num_of_drinks):
        drink = sys.stdin.readline().strip()
        relationships_of_drinks.update({drink: [0,[]]})
    num_relations = int(sys.stdin.readline())

    for i in range(num_relations):
        relation1, relation2 = sys.stdin.readline().split()
        relationships_of_drinks.get(relation1)[1].append(relation2)
        relationships_of_drinks.get(relation2)[0] += 1

    while relationships_of_drinks:
        for drink in relationships_of_drinks:
            if relationships_of_drinks.get(drink)[0] == 0:
                drink_list += (drink + " ")
                for child in relationships_of_drinks.get(drink)[1]:
                    relationships_of_drinks.get(child)[0] -= 1
                relationships_of_drinks.pop(drink)
                break
    drink_list = drink_list[:len(drink_list) - 1]
    drink_list += "."

    print("Case #" + str(case_number) + ": " + drink_list)
    print("")
    sys.stdin.readline()
