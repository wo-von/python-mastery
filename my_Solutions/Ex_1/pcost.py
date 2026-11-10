#!/usr/bin/python3
ROOT_PATH = "../../"

DATA_PATH = ROOT_PATH + "Data/"

DATA_SOURCE = "portfolio.dat"


def totalCost(data_path):
    total_cost = 0
    with open(data_path) as f:
        for line in f:
            shares = int(line.split()[1])
            cost = float(line.split()[2])
            total_cost += shares * cost
    return total_cost


print(totalCost(DATA_PATH + DATA_SOURCE))
