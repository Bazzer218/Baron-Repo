#!/usr/bin/python3

def evens(n):
    return list(filter(lambda t: t % 2 == 0, range(n+1)))
