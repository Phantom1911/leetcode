# https://www.hackerrank.com/challenges/picking-numbers/problem

from collections import Counter


def pickingNumbers(a):
    # Write your code here
    counter = Counter(a)
    sorted_keys = sorted(counter.keys())
    maximum = -1
    for key in sorted_keys:
        maximum = max(maximum, counter[key] + counter[key + 1])

    return maximum