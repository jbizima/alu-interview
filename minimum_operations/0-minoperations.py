#!/usr/bin/python3

"""
Solution for the following problem:

In a text file, there is a single character H. Your text editor can execute only two
operations in this file: Copy All and Paste. Given a number n, write a method that
calculates the fewest number of operations needed to result in exactly n H characters
in the file.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H
    characters in the file.

    Args:
        n: an integer representing the number of H characters desired in the file.

    Returns:
        An integer representing the fewest number of operations needed, or 0 if n
        is not possible to achieve.
    """
    if n <= 0:
        return 0
    operations = 0
    for i in range(2, n + 1):
        while n % i == 0:
            operations += i
            n /= i
    return operations if n == 1 else 0
