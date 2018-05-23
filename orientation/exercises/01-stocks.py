# stock symbol dictionary
stocks = {
    'GOOGL': 'Alphabet Inc.',
    'AAPL': 'Apple Inc.',
    'MSFT': 'Microsoft Corp.'
}

# symbol, quantity, date, price
purchases = [
    ('GOOGL', 5, '10-sep-2001', 1082.38),
    ('AAPL', 10, '1-apr-1999', 187.57),
    ('MSFT', 20, '1-jul-1998', 98.13)
]

# map two lists into one with name of stock and total value
report = map(lambda tup: (stocks[tup[0]], tup[1]*tup[3]), purchases)

# print nicely
for item in report:
    print item[0] + '\t\t$ ' + str(item[1])