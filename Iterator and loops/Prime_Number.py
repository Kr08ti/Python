#to check a given number is prime or not
num = 10
#prime number are greater then one
if num > 1:
    for i in range(2,5):
        if (num % i) == 0:
            print "the number is not prime"
            break
    else:
        print("the number is prime", 5)
#else:
#    print "the number is prime"

