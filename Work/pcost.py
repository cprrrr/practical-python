# pcost.py
#
# Exercise 1.27
import sys
import report

def portfolio_cost(filename, types: list = None):
    tab = report.read_portfolio(filename=filename, types=types)
    cost = 0
    for row in tab:
        cost += row['shares']*row['price']
    return cost

if len(sys.argv) == 2:
    file = sys.argv[1]
else:
    file = 'D:/adastra/playground/pythontuto/practical-python/Work/Data/missing.csv'
print(f'Total cost: {portfolio_cost(file, types=[str, int, float]):0.2f}')

