# pcost.py
#
# Exercise 1.27
import sys
import report

def portfolio_cost(filename, types: list = [str, int, float]):
    tab = report.read_portfolio(filename=filename, types=types)
    cost = 0
    for row in tab:
        cost += row.shares*row.price
    return cost
def main(argv: list):
    if len(argv) == 2:
        f = str(argv[1])
        c = portfolio_cost(f)
        print('Total cost is:', c)

    elif len(argv) > 2:
        f = str(argv[1])
        types = argv[2:]
        c = portfolio_cost(f, types = types)
        print('Total cost is:', c)


if __name__ == '__main__':
    import sys
    main(sys.argv)



