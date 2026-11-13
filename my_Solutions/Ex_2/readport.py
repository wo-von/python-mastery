import csv


def read_portfolio(filename):
    portfolio = list()
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            position = {
                "name": row[0],
                "shares": int(row[1]),
                "price": float(row[2]),
            }
            portfolio.append(position)
    return portfolio
