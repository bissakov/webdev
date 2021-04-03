x = int(input())
a = 0

for i in range(1,x+1):
    if x % i == 0: a += 1

print(a)