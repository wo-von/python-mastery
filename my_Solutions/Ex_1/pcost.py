#!/usr/bin/python3
ROOT_PATH = "../../"

DATA_PATH = ROOT_PATH + "Data/"
DEFAULT_DATA = "portfolio1.dat"


def portfolio_cost(data_path):
    data_path = DATA_PATH + data_path
    total_cost = 0
    with open(data_path) as f:
        for line in f:
            linelst = line.split()
            try:
                shares = int(linelst[1])
                cost = float(linelst[2])
                total_cost += shares * cost
            except ValueError as e:
                print(f"Couldn't parse {line}Reason: {e}")
                continue
    return total_cost


if __name__ == "__main__":
    print(portfolio_cost(DEFAULT_DATA))
