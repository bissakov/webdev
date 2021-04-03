n = int(input())
zero = 0

for i in range(1,n+1):
    nums = int(input())
    if nums == 0: zero += 1

print(zero)