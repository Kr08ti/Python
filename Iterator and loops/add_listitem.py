def add_list_elements(num):
    add = 0
    for i in num:
        add=add+i
    print add
num = [1,2,3,4]
add_list_elements(num)


def add_list(*args):
    number = 0
    for x in args :
        number=number+x
    print number
x = range(1,10)
add_list(*x)

sum = 0
for i in range(0, 5):
    sum = sum + i
print sum

#from math import sum
#a = [1,2,3,4,5]
#b = sum(a)
#print(b)