# fileparse.py
#
# Exercise 3.3

import csv
from collections.abc import Iterable

def parse_csv(iname: Iterable, select: list = None, types: list = None, delimit: str = None,has_headers = True, silence_errors=False) -> list:

    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")

    if not isinstance(iname, Iterable):
        raise ValueError(f"{iname} is not iterable")

    if delimit:  # if specify delimiter
        rows = csv.reader(iname, delimiter=delimit)
    else:
        rows = csv.reader(iname)

    records = []
    if has_headers: # with headers
        headers = next(rows)
        if select:  # if select fields
            indices = [headers.index(x) for x in select]
        else:
            select = headers
            indices = [headers.index(x) for x in select]

        for no, row in enumerate(rows):  # work through
            if not row: # skip blank row
                continue
            else:
                try:
                    if types:
                        record = {headers[x]: t(row[x]) for t, x in zip(types, indices)}
                    else:
                        record = {headers[x]: row[x] for x in indices}
                    records.append(record)
                except ValueError as e:
                    if silence_errors:
                        continue
                    else:
                        print(f"Row {no:d}: Couldn't convert {row} \nReason: {e}")
                        continue

    else: # without headers
        for no, row in enumerate(rows):  # work through
            if not row:  # skip blank row
                continue
            else:
                try:
                    if types:
                        record = tuple([a(b) for a, b in zip(types, row)])
                    else:
                        record = (row[0], row[1])
                    records.append(record)
                except ValueError as e:
                    if silence_errors:
                        continue
                    else:
                        print(f"Row {no:d}: Couldn't convert {row} \nReason: {e}")
                        continue

    return records




