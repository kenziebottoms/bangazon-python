# Python Planet List

## Reference

* [Python Lists](https://docs.python.org/3.6/tutorial/datastructures.html)
* [Learn Python - Lists](http://www.learnpython.org/en/Lists)

## Starting code

```py
planet_list = ["Mercury", "Mars"]
```

## Exercise

- [x] Use `append()` to add Jupiter and Saturn at the end of the list.
- [x] Use the `extend()` method to add another list of the last two planets in our solar system to the end of the list.
- [x] Use `insert()` to add Earth, and Venus in the correct order.
- [x] Use `append()` again to add Pluto to the end of the list.
- [x] Now that all the planets are in the list, slice the list in order to get the rocky planets into a new list called `rocky_planets`.
- [x] Being good amateur astronomers, we know that Pluto is now a dwarf planet, so use the `del` operation to remove it from the end of `planet_list`.

## Iterating over planets

- [x] Create another list containing tuples. Each tuple will hold the name of a spacecraft that we have launched, and the names of the planet(s) that it has visited, or landed on. (e.g. `('Cassini', 'Saturn')`).
- [x] Iterate over your list of planets, and inside that loop, iterate over the list of tuples. Print, for each planet, which satellites have visited. 