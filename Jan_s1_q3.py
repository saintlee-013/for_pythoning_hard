t = (1,2,3,4)
tl = []
tl = list(t)
leng = len(tl)
mid = leng//2
tl_f = tl.pop(mid)
tl_s = tl.pop(mid-1)
print(tl_f)
print(tl_s)
tl.insert(0,tl_s)
tl.insert(leng-1, tl_f)
print (tuple(tl))

