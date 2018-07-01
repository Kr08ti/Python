L1 = [1, 2, 3, 4]
print L1

#L1.append(90)
#print L1

L2 = [1, 4, 9, 10 ,23]
sl1 = L2[1:3]
sl2 = L2[3:5]
sl3 = L2[-1]

print sl1
print sl2
print sl3

addition = sum(L2)
print "The addition is:", addition

del L2[1:3]

print "The index [4,9] is deleted from the L2 list and now the values are:", L2

