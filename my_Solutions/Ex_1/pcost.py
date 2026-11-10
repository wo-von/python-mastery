#!/usr/bin/python3
ROOT_PATH = "../../"

DATA_PATH = ROOT_PATH + "Data/"

DATA_SOURCE = "portfolio.dat"
BAD_DATA_SOURCE = "portfolio3.dat"


def totalCost(data_path):
    total_cost = 0
    with open(data_path) as f:
        for line in f:
            try:
                shares = int(line.split()[1])
            except ValueError as e:
                print(f"Couldn't parse {line}Reason: {e}")
                continue
            try:
                cost = float(line.split()[2])
            except ValueError as e:
                print(f"Couldn't parse {line}Reason: {e}")
                continue
            total_cost += shares * cost
    return total_cost


print(totalCost(DATA_PATH + DATA_SOURCE))
print(totalCost(DATA_PATH + BAD_DATA_SOURCE))
