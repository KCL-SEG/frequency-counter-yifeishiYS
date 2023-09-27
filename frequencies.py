"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for key in items:
        key = str(key)
        if key not in frequencies:
            frequencies[key] = 1
        else:
            frequencies[key] += 1
    return frequencies
