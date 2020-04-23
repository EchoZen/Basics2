#Requires multiple passes, gets the largest value to the end of the list first
#My own sorting algorithm
numbers= [50,22,10,15,44,32]
for i in range(len(numbers)):
    for i in range(0,len(numbers)-1):
        if numbers[i]>numbers[i+1]:
            a= numbers[i+1]
            numbers[i+1]= numbers[i]
            numbers[i]=a
print(numbers)
#sorting function by SBS
# #To make the program even more efficient,
# 1) reduce number of passes through the loop
# 2) check if the list is already sorted so the program does not sort unneccesarily
num=[0,1,2,3,4,5,6]
def bubbleSort(alist):
    for passnum in range(len(alist)-1):
        # This increases the efficiency as less items have to be sorted (1)
        # On average, the inner loop runs n/2 each time outer loop runs
        swapped= False #To check if list is already sorted (2)
        for i in range(len(alist)-passnum-1):
            if alist[i]>alist[i+1]:
                a= alist[i]
                alist[i]= alist[i+1]
                alist[i+1]= a
                swapped= True
        print("pass", passnum+1, ":", alist)
        if not swapped:
            break

bubbleSort(num)
