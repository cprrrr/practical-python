# tableformat.py

class TableFormatter(object):
    def headings(self, headers):
        raise NotImplementedError()

    def row(self, rowdata):
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers: list):
        for i in headers:
            print(f"{i:>10s}", end=' ')
        print('')
        print(('-'*10+' ')*len(headers))

    def row(self, rowdata: list):
        for i in rowdata:
            print(f"{i:>10s}", end=' ')
        print('')

class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print('<tr>', end='')
        for i in headers:
            print(f"<th>{i}</th>", end='')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end='')
        for i in rowdata:
            print(f"<td>{i}</td>", end='')
        print('</tr>')

class FormatError(Exception):
    pass

def create_formatter(name: str):
    if name == 'txt':
        formatter = TextTableFormatter()
    elif name == 'csv':
        formatter = CSVTableFormatter()
    elif name == 'html':
        formatter = HTMLTableFormatter()
    else:
        raise FormatError(f"Unknown table format '{name}'")

    return formatter

def print_table(datatab: list, selects: list, fmt: TableFormatter):
    fmt.headings(selects)
    for s in datatab:
        fmt.row([str(getattr(s, i)) for i in selects])








