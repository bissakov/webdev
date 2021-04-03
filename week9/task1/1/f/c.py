def xor(a,b):
    if a == 0 or a == 1 and b == 0 or b == 1:
        if a == b: return(0)
        else: return(1)

l = input().split(" ")

print( xor(int(l[0]),int(l[1])) )