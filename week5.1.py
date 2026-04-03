#find the minimum in a list, append it to another, delete the element from original list
def sorting(l):
    x = []

    while (len(l)>0):
        min = l[0]
        min_index= 0
        for i in range(len(l)):
            if(l[i]<min):
                min = l[i]
                min_index = i
        popped = l.pop(min_index)
        x.append(popped)

    return x
l = [4,3,25,6,2,11]
print(sorting(l))
