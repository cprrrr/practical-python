# pcost.py
#
# Exercise 1.27
import sys
import csv

def portfolio_cost(filename):
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    cost = 0

    for rowno, row in enumerate(rows):
        dic = dict(zip(headers, row))
        try:
            num = int(dic['shares'])
            price = float(dic['price'])
            cost += num * price
        except ValueError:
            print(f"Row {rowno+1:d}: Coundn't convert:", row)
            continue
    f.close()
    return cost

if len(sys.argv) == 2:
    file = sys.argv[1]
else:
    file = 'D:/adastra/playground/pythontuto/practical-python/Work/Data/missing.csv'
print(f'Total cost: {portfolio_cost(file):0.2f}')

