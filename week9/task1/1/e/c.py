n = int(input())
a = input().split(" ")

x = 0

for i in a:
    if int(i) > 0: x += 1

print(x)