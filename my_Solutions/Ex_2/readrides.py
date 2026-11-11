import csv
import typing


class Row:
    __slots__ = ["route", "date", "daytype", "rides"]

    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


class Row_t(typing.NamedTuple):
    route: str
    date: str
    daytype: str
    rides: int


def read_rides_as_tuples(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records


def read_rides_as_class_with_slots(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(f)
        for row in rows:
            row = Row(row[0], row[1], row[2], int(row[3]))
            records.append(row)
    return records


def read_rides_as_dicts(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {}
            record["route"] = route
            record["date"] = date
            record["daytype"] = daytype
            record["rides"] = rides
            records.append(record)
    return records


def read_rides_as_named_tuple(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Row_t(route, date, daytype, rides)
            records.append(record)
    return records


if __name__ == "__main__":
    import tracemalloc

    tracemalloc.start()
    rows = read_rides_as_tuples("../../Data/ctabus.csv")
    print("Memory usage: current %d, peak %d" % tracemalloc.get_traced_memory())
