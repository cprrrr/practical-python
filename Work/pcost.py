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
    for row in rows:
        try:
            num = int(row[1])
            price = float(row[2])
            cost += num * price
        except ValueError:
            print('something is wrong->', row)
            continue
    f.close()
    return cost

if len(sys.argv) == 2:
    file = sys.argv[1]
else:
    file = 'D:/adastra/playground/pythontuto/practical-python/Work/Data/portfolio.csv'
print(f'Total cost: {portfolio_cost(file):0.2f}')

