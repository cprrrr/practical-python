# ticker.py

from follow import follow
import csv
import report

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    return rows

def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def convert_types(rows, types):
    for row in rows:
        yield [t(d) for t, d in zip(types, row)]

def make_dicts(rows, headers):
    return (dict(zip(headers, row)) for row in rows)


def ticker(portfile, logfile, fmt):
    portfolio = report.read_portfolio(portfile)
    formatter = report.tableformat.create_formatter(fmt)

    lines = follow(logfile)
    rows = parse_stock_data(lines)
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    rows = (row for row in rows if row['name'] in portfolio )

    tab = {}
    for i, row in enumerate(rows):
        tab[row['name']] = [row['price'], row['change']]
        if (i+1)%3 == 0:
            formatter.headings(['Name', 'Price', 'Change'])
            for name in tab:
                rowdata = [name, f'{tab[name][0]:0.2f}', f'{tab[name][1]:0.2f}']
                formatter.row(rowdata)
            print('')



if __name__ == '__main__':
    lines = follow('Data/stocklog.csv')
    rows = parse_stock_data(lines)
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    for row in rows:
        print(row)