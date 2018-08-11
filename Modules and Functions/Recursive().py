def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)
print factorial(6)

def fibo(n):
    a = 0
    b = 1
    c = []
    while b < n:
        c.append(b)
        temp = a
        a = b
        b = temp+a
    print c
fibo(9)

def fib(n):
    x = 0
    y = 1
    while y < n:
        temp = x
        x = y
        y = temp + x
    return n
print(fibo(50))


def interger(num):
    n = 0
    add = n + num
    print add
interger(10)

