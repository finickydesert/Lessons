#!/usr/bin/env python3
#remember to have the function 'def' before the call
#the formula for def function_name (parameter_name)
""""you need to have a parameter or you eill get an error"""
def say_hi(name = 'there'):
    print('Hi {}!'.format(name))
say_hi()
say_hi('Bob')
def say_bye(first, last = 'doe'):
    print('hi {} {}!'.format(first, last))
say_bye('jane')
say_bye('john','smith')