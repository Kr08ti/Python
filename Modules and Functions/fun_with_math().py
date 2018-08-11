import math

log_list = [1, 2, 6, 9 ,15]
loggy = []
for i in log_list:
    base_log = math.log(i)
    loggy.append(base_log)
print loggy
print log_list

from fractions import gcd
n = gcd(15, 21)
print n

m = gcd(152, 200)
print m

