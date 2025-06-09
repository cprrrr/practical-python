# report.py
#
# Exercise 2.4
import sys
import csv

def read_portfolio(filename: str)->list:
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows):
            dic = dict(zip(headers, row))
            try:
                tickle = str(dic['name'])
                num = int(dic['shares'])
                price = float(dic['price'])
                portfolio.append({'name' : tickle, 'shares' : num, 'price' : price})
            except ValueError:
                print('something is wrong in '+str(filename)+'->', row)
                continue
    return portfolio

def read_endprice(filename: str)->dict:
    dic = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                name = str(row[0])
                p = float(row[1])
                dic[name] = p
            except (ValueError, IndexError) as error:
                print('something is wrong in '+str(filename)+'->', row)
                continue
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
    portfolio = read_portfolio(filename)
    endprice = read_endprice(pricefilename)
    table = make_report(portfolio, endprice)
    print_report(table)


if len(sys.argv) == 2:
    file1 = sys.argv[1]
    file2 = 'Data/prices.csv'
elif len(sys.argv) == 3:
    file1 =sys.argv[1]
    file2 = sys.argv[2]
elif len(sys.argv) == 1:
    file1 = 'D:/adastra/playground/pythontuto/practical-python/Work/Data/portfolio.csv'
    file2 = 'Data/prices.csv'
else:
    raise TypeError ('extra input')

portfolio_report(file1, file2)


