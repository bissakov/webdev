import math

a = int(input())
b = int(input())

for i in range(a,b+1):
    x = int(math.sqrt(i))
    if x*x == i: print(i)