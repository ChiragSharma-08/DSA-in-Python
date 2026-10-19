def fib(n):

    # if fib(1) or fib(2)
    if n==1 or n==2:
        return 1

    # anu other position = prev + position before that
    return fib(n-1)+fib(n-2)

print(fib(8))