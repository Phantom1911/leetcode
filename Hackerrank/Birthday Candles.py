# https://www.hackerrank.com/challenges/birthday-cake-candles/problem

def birthdayCakeCandles(candles):
    # Write your code here
    maximum = max(candles)
    count = 0
    for i in range(len(candles)):
        if candles[i] == maximum:
            count +=1
    return count