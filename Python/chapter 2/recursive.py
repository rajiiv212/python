from audioop import add
from tkinter import Y


def rec(k):
    if(k>0):
        result = k + rec(k-1)
        print(result)
    else:
        result=0
    return result
print("rec")
rec(7)


def shout(text):
    return text.upper()

def yell(text):
    return text.lower()

def greet(func):
    greeting = func("hello this is python")
    print(greeting)
greet(shout)
greet(yell)


def create_adder(x):
    def adder(y):
        return x+y
    return adder
add_15 = create_adder(15)
print(add_15(10))