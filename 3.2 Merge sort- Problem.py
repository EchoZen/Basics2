
list = [8,9,4,6,10]

#Use recursion
#First split the damn list

def mergesort(list):
    length= len(list)
    if length==1:
        return list
    else:
        left= list[:list[length//2]]
        right= list[list[length//2]:]
        left= mergesort(left)
        right= mergesort(right)
    return merge(left, right)

def merge(left, right):
    for i in range(len(left)):
        if left[i]<right[i]:
            left.append(right[i])
            right.remove(right[i])
        else:
            right.append(left[i])
            left.remove(left[i])
print(mergesort(list))
#Use for loop