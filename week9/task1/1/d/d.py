def isTwo(x):
    if x == 1: return("YES")
    if x < 1: return("NO")

    while x >= 1:
        if x == 1: return("YES")
        if x % 2 == 0: x = x / 2
        else: return("NO")

n = int(input())

print(isTwo(n))