# def fibo(n):
#     a, b = 0 , 1
#     while b < n:
#         print b
#         a, b = b, a+b
#
# fibo(20)

# prints fibonnaci series
def fib(num):
    a = 0
    b = 1
    c = []
    while b < num:
        c.append(b)
        temp = a
        a = b
        b = temp+a
    print c
fib(20)