# report.py
#
# Exercise 2.4
import sys
import fileparse
import stock
import tableformat
from portfolio import Portfolio
from stock import Stock


def read_portfolio(filename, **opts):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename) as file:
        portfolio = Portfolio.from_csv(file, **opts)
    return portfolio


def read_endprice(filename: str, select: list = None, types: list = None, delimit: str = None,
                  silence_errors=False) -> dict:
    with open(filename, 'rt') as f:
        dic = fileparse.parse_csv(iname=f, select=select, types=types, delimit=delimit, has_headers=False,
                                  silence_errors=silence_errors)
    dic = dict(dic)
    return dic


def make_report(lisostock: Portfolio, dicoprice: dict) -> list:
    rows = []
    for stock in lisostock:
        try:
            change = float(dicoprice[stock.name] - stock.price)
        except Exception as e:
            change = 0
        rows.append((stock.name, stock.shares, dicoprice[stock.name], change))
    return rows


def print_report(tab: list, formatter: tableformat.TableFormatter):
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in tab:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)


def portfolio_report(filename: str, pricefilename='Data/prices.csv', fmt: str = 'txt'):
    portfolio = read_portfolio(filename)
    endprice = read_endprice(pricefilename, types=[str, float])
    table = make_report(portfolio, endprice)

    formatter = tableformat.create_formatter(fmt)
    print_report(table, formatter)


def main(argv: list):
    f1 = str(argv[1])
    f2 = str(argv[2])
    fom = str(argv[3])
    portfolio_report(f1, f2, fom)


if __name__ == '__main__':
    import sys

    main(sys.argv)
