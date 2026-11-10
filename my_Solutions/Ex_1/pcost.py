#!/usr/bin/python3
ROOT_PATH = "../../"

DATA_PATH = ROOT_PATH + "Data/"

DATA_SOURCE = "portfolio.csv"

with open(DATA_PATH + DATA_SOURCE) as f:
    data = f.read()

datalst = data.split("\n")[:-1]

header = datalst[0]

cost = 0

for l in range(len(datalst)):
    if l == 0:
        continue
    cost += int(datalst[l].split(",")[1]) * float(datalst[l].split(",")[2])

print(cost)
