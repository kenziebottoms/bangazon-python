# Python Car Sets

## References

* [Python sets](https://docs.python.org/3.6/tutorial/datastructures.html#sets)
* [Set intersection](https://docs.python.org/3.6/library/stdtypes.html?highlight=intersection#set.intersection)
* [Learn Python - Sets](http://www.learnpython.org/en/Sets)

## Instructions

- [x] Create an empty set named `showroom`.
- [x] Add four of your favorite car model names to the set.
- [x] Print the length of your set.
- [x] Pick one of the items in your show room and add it to the set again.
- [x] Print your showroom. Notice how there's still only one instance of that model in there.
- [x] Using `update()`, add two more car models to your showroom with another set.
- [x] You've sold one of your cars. Remove it from the set with the `discard()` method.

### Acquiring more cars

- [x] Now create another set of cars in a variable `junkyard`. Someone who owns a junkyard full of old cars has approached you about buying the entire inventory. In the new set, add some different cars, but also add a few that are the same as in the `showroom` set.
- [x] Use the `intersection` method to see which cars exist in both the showroom and that junkyard.
- [x] Now you're ready to buy the cars in the junkyard. Use the `union` method to combine the junkyard into your showroom.
- [x] Use the `discard()` method to remove any cars that you acquired from the junkyard that you want in your showroom.