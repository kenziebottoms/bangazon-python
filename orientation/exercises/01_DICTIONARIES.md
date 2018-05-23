# Python Stock Dictionary

## References

* [Python dictionaries](https://docs.python.org/3.6/tutorial/datastructures.html#dictionaries)
* [Learn Python - Dictionaries](https://www.learnpython.org/en/Dictionaries)
* [Introducing Dictionries](http://www.diveintopython.net/native_data_types/index.html#odbchelper.dict)


## Instructions

A block of publicly traded stock has a variety of attributes, we'll look at a few of them. A stock has a ticker symbol and a company name. 

- [x] Create a simple dictionary with ticker symbols and company names.

##### Example

```python
stockDict = { 'GM': 'General Motors',
 'CAT':'Caterpillar', 'EK':"Eastman Kodak" }
```

- [x] Create a simple list of blocks of stock. These could be tuples with ticker symbols, number of shares, dates and price.

##### Example

```python
purchases = [ ( 'GE', 100, '10-sep-2001', 48 ),
 ( 'CAT', 100, '1-apr-1999', 24 ),
 ( 'GE', 200, '1-jul-1998', 56 ) ]
```

1. Create a purchase history report that
    - [x] computes the full purchase price (shares times dollars) for each block of stock,
    - [x] uses the `stockDict` to look up the full company name.

      This is the basic relational database join algorithm between two tables.

2. Create a second purchase summary that
    - [ ] accumulates total investment by ticker symbol.
