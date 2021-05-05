 Starred Expression
 ```python3
 >>> numbers = [2, 1, 3, 4, 7]
>>> more_numbers = [*numbers, 11, 18]
>>> print(*more_numbers, sep=', ')
2, 1, 3, 4, 7, 11, 18
```
Using * to unpack iterables into a list/tuple
Using ** to unpack dictionaries into other dictionaries

## Sudoku Question

1. **Iterate a 2D Array**
```python3
>>> theArray = [
  ['a','b','c'],
  ['d','e','f'],
  ['g','h','i']
  ]
>>> zip(*theArray)
[('a', 'd', 'g'), ('b', 'e', 'h'), ('c', 'f', 'i')]
```
>Unpacked the list in zip function hence can be itterated

2. **Check if Element is unique in list**
```python3
>>> your_list = ['one', 'two', 'one']
>>> len(your_list) != len(set(your_list))
True
```
> Set has only unique elements hence we converted list to set and compared both list and set length
