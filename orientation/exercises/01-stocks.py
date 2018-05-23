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
    ('MSFT', 10, '1-jul-1998', 98.13),
    ('MSFT', 10, '1-jul-2001', 97.42)
]

# map two lists into one with name of stock and total value
report = map(lambda tup: (stocks[tup[0]], tup[1]*tup[3]), purchases)

# total up stocks by symbol
totals = {}
for i in range(0, len(purchases)):
    # if this is already in the dictionary, add to its value
    if purchases[i][0] in list(totals.keys()):
        totals[purchases[i][0]] += report[i][1]
    else:
        totals[purchases[i][0]] = report[i][1]

# print report nicely
print '--- PURCHASES ---'
for item in report:
    print item[0] + '\t\t$ ' + str(item[1])

# print totals nicely
print '\n--- TOTALS ---'
for key, value in totals.items():
    print key + '\t\t\t$ ' + str(value)