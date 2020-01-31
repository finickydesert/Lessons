#!/bin/python3
#i wrote this script with a few divergances
#from: https://projects.raspberrypi.org/en/projects/about-me 
print("hello\nmy name is richard herist\ncurrently i am creating the script so i get one lesson done today.\n")
print("if you need to know me check out my linkedin!\n")
birthyear = int(input("to find out if your old enough to drink (year wise) please type your birth year: "\n))
age = 2020 - birthyear
age1 = str(age)
aged = str(age * 7)
time = str(21 - age)
timed = str(float(21 - age) * 7)
if age >= 21:
    print("your old enough, also you re " + age1)
    print("in dog years you are: " + aged + "\n")

else:
    print ("you got to wait " + time + " more years for that")
    print("it is going to take you " + timed + " years in dog years just to drink\n")

print("also here is my dog:")
print(" ")
print("<ô")
print("  (-------)----")
print("   ||    ||")

