l1 = [11, 2, 3]
l3 = []
for i in range(3):
    if l1[-1] > l1[0]:
        l3.append(l1[-1])
    elif l1[0] > l1[-1]:
        l3.append(l1[0])
    else:
        print l1
print l3
