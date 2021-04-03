n = int(input())

k = 0
while n > 1:
    k += 1
    n = (n + 1) // 2

print(k)