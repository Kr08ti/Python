#def example():
    #num=[range(10)]
    #for i in num:
    #    num.append(i*i)
    #    print num

#example()

num = 100
for count in range(1, num):
    if count%3 == 0 and count%5 == 0:
        print "FizzBuzz"
    elif count%3 == 0:
        print "Fizz"
    elif count%5 == 0:
        print "Buzz"
    else:
        print count