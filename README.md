# 1_take_skip_iterators_and_generators_exercise
Create a class called take_skip. Upon initialization, it should receive a step (int) and a count (int). Implement the __iter__ and __next__ functions. The iterator should return the count numbers (starting from 0) with the given step. For more clarification, see the examples:

Test Code
numbers = take_skip(2, 6)
for number in numbers:
    print(number)

Output

0
2
4
6
8
10
