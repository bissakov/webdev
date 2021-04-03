def pw(x,y):
    if y == 0: return(0)
    i = 1
    a = x
    while i < y:
        a *= x
        i += 1
    if int(a) == a:
        return(int(a))
    return(a)

l = input().split(" ")

if int(l[1]) > 0:
    print(pw(float(l[0]),int(l[1])))