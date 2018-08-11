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


def count_evens(nums):
  l1 = []
  for i in range(len(nums)):
    if nums[i]%2 == 0:
      l1.append(nums[i])
  print len(l1)
count_evens([2, 1, 2, 3, 4])