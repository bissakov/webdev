def f(l):
    for i in range(1,len(l)):
        if int(l[i]) > 0 and int(l[i-1]) > 0 or int(l[i]) < 0 and int(l[i-1]) < 0:
            return("YES")

    return("NO")

n = int(input())
a = input().split(" ")

print(f(a))