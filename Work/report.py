# report.py
#
# Exercise 2.4
import sys
import fileparse


def read_portfolio(filename: str, select: list = None, types: list = None, delimit: str = None, silence_errors=False)->list:
    with open(filename, 'rt') as f:
        portfolio = fileparse.parse_csv(iname=f, select=select, types=types, delimit=delimit, has_headers=True, silence_errors=silence_errors)
    return portfolio

def read_endprice(filename: str, select: list = None, types: list = None, delimit: str = None, silence_errors=False)->dict:
    with open(filename, 'rt') as f:
        dic = fileparse.parse_csv(iname=f, select=select, types=types, delimit=delimit, has_headers=False, silence_errors=silence_errors)
    dic = dict(dic)
    return dic

def make_report(lisostock: list, dicoprice: dict)->list:
    rows = []
    for stock in lisostock:
        change = float(dicoprice[stock['name']] - stock['price'])
        rows.append((stock['name'], stock['shares'], dicoprice[stock['name']], change))
    return rows

def print_report(tab: list):
    print(f"\n{'Name':>10s} {'Shares':>10s} {'Price':>10s} {'Change':>10s}")
    print(('-' * 10 + ' ') * 4)
    gl = 0
    for i in tab:
        print(f"{i[0]:>10s} {i[1]:>10d} {'$' + str(round(i[2], 2)):>10s} {'$' + str(round(i[3], 2)):>10s}")
        gl += i[1] * i[3]
    print(f'\ntotal gain/loss: ${gl:0.2f}')

def portfolio_report(filename: str, pricefilename='Data/prices.csv'):
    portfolio = read_portfolio(filename, types = [str, int, float])
    endprice = read_endprice(pricefilename, types = [str, float])
    table = make_report(portfolio, endprice)
    print_report(table)

def main(argv: list):
    f1 = str(argv[1])
    f2 = str(argv[2])
    portfolio_report(f1, f2)


if __name__ == '__main__':
    import sys
    main(sys.argv)



