# fileparse.py
#
# Exercise 3.3

import csv

def csv_parse(filename: str, select: list = None, types: list = None, delimit: str = None,has_headers = True) -> list:
    '''
    parse a csv file into a list of records (list of dicts)
    :param filename:
    :param select:
    :param types:
    :param delimit:
    :return:
    '''
    with open(filename) as f:
        if delimit:  # if specify delimiter
            rows = csv.reader(f, delimiter=delimit)
        else:
            rows = csv.reader(f)

        records = []
        if has_headers: # with headers
            headers = next(rows)
            if select:  # if select fields
                pass
            else:
                select = headers
            try:
                indices = [headers.index(x) for x in select]
            except ValueError:
                print("file only contains:", indices)

            for row in rows:  # work through
                if not row:  # skip blank row
                    continue
                else:
                    if types:
                        record = {headers[x]: t(row[x]) for t, x in zip(types, indices)}
                    else:
                        record = {headers[x]: row[x] for x in indices}
                    records.append(record)

        else: # without headers
            for row in rows:  # work through
                if not row:  # skip blank row
                    continue
                else:
                    record = tuple([a(b) for a, b in zip(types, row)])
                    records.append(record)

    return records
