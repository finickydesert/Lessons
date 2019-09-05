#!/usr/bin/env python3
#making a table
print('{0:8} | {1:8}'.format("fruit", "quantity"))
print('{0:8} | {1:8}'.format("apple",3))
print('{0:8} | {1:8}'.format("orange", 10)
#to control alignment use < for left, ^ for center, > right
print('{0:8} | {1:<8}'.format("fruit", "how much?"))
print('{0:8} | {1:<8}'.format("apple",3))
print('{0:8} | {1:<8}'.format("orange", 10))
answer = input("enter a name of a fruit: ")
print("{} is a lovely fruit.".format(answer))