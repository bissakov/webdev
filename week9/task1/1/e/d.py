n = int(input())
a = input().split(" ")

x = 0

for i in range(1,len(a)):
    if a[i] > a[i-1]: x += 1

print(x)