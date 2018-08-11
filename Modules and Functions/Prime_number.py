#a function that takes an argument for prime number

def prime(n):
    if n > 1: #prime numbers are greater than one
        for i in range(2,n):
            if (n % i) == 0:
                print("The number is not prime", n)
                break #ends the for loop
        else:
            print("The number is prime", n)
    else:
        print("The number is not prime")
num = -1
prime(num)
