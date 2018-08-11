#find the factorial of a given number
num = 6
factorial = 1

if num < 0:
    print "The number is negative"
elif num == 0:
    print "The factorial of 0 is 1"
else:
    for i in range (1, num+1):
        factorial = factorial*i
    print "The factorila of",num,"is:",factorial
