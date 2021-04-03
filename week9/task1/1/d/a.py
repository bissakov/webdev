import math

n = int(input())

# for i in range(1,int(math.sqrt(n))+1):
#     print(i*i)

i = 1
while i <= int(math.sqrt(n)):
    print(i*i)
    i += 1