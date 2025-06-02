# report.py
#
# Exercise 2.4
import sys
import csv

def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                tickle = str(row[0])
                num = int(row[1])
                price = float(row[2])
                portfolio.append({'name' : tickle, 'shares' : num, 'price' : price})
            except ValueError:
                print('something is wrong->', row)
                continue
    return portfolio

def read_endprice(filename):
    dic = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                name = str(row[0])
                p = float(row[1])
                dic[name] = p
            except (ValueError, IndexError) as error:
                print('something is wrong->', row)
                continue
    return dic

if len(sys.argv) == 2:
    file = sys.argv[1]
else:
    file = 'D:/adastra/playground/pythontuto/practical-python/Work/Data/portfolio.csv'
portfolio = read_portfolio(file)
endprice = read_endprice('Data/prices.csv')

sp = 0
ep = 0
for stock in portfolio:
    stock['endprice'] = endprice[stock['name']]
    sp += stock['shares'] * stock['price']
    ep += stock['shares'] * stock['endprice']
    print(stock)

print(f'total gain/loss:{ep - sp:0.2f}')


