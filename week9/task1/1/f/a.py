def minOf2(x,y):
    if x < y: return x
    else: return y

def minOf4(a,b,c,d):
    print(minOf2(minOf2(a,b),minOf2(c,d)))

l = input().split(" ")

minOf4(l[0],l[1],l[2],l[3])
