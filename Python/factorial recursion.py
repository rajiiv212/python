from tkinter import N


def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)

print(fact(7))