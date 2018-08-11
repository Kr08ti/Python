# find the factors of a given number

def factor(x):
    print "The factor of the given number:", num,"are:"
    for i in range(1,x+1):
        if x % i == 0:
            print i

num = 6
factor(num)