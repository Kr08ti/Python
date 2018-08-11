def odd_even():
    
   for i in list(range(10)):
    if i%2 == 0:
       print "even", i
    else:
       print "odd", i

odd_even()


n = int(raw_input())
if n%2 != 0:
    print "weird"
else:
    if n%2 == 0 and (n in range(2,5) or n > 20):
        print("Not Weird")
    elif n%2 == 0 and (n in range(6,20)):
        print("Weird")
    else:
        pass
