if __name__=="__main__":
    fib = 0
    x = 1
    y = 2
    sum = 2
    i = 3
    while fib <= 4000000:
        fib = x + y
        x = y
        y = fib
        if i % 2 == 0 and fib <= 4000000:
            sum += fib
        i+=1
    print(sum)

