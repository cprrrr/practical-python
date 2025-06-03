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
                print('something is wrong in '+str(filename)+'->', row)
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
                print('something is wrong in '+str(filename)+'->', row)
                continue
    return dic

def make_report(lisostock, dicoprice):
    rows = []
    for stock in lisostock:
        change = float(dicoprice[stock['name']] - stock['price'])
        rows.append((stock['name'], stock['shares'], dicoprice[stock['name']], change))
    return rows

if len(sys.argv) == 2:
    file = sys.argv[1]
else:
    file = 'D:/adastra/playground/pythontuto/practical-python/Work/Data/portfolio.csv'
portfolio = read_portfolio(file)
endprice = read_endprice('Data/prices.csv')
table = make_report(portfolio, endprice)

print(f"\n{'Name':>10s} {'Shares':>10s} {'Price':>10s} {'Change':>10s}")
print(('-' * 10 + ' ') * 4)
gl = 0
for i in table:
    print(f"{i[0]:>10s} {i[1]:>10d} {'$'+str(round(i[2], 2)):>10s} {'$'+str(round(i[3], 2)):>10s}")
    gl += i[1] * i[3]

print(f'\ntotal gain/loss: ${gl:0.2f}')


