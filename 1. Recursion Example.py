#Difference btwn for loop and recursion

#For loop
def factorial(number):
    product=1
    for i in range(number):
        product= product*(i+1)
    return product

#Recursive loop
def factorialR(number):
    if number==1:
        return 1
    else:
        return number*factorialR(number-1)

#Tower of Hanoi
list1=[1,2,3,4]
list2=[]
list3=[]
#Goal is to change list1 to list3 by moving the numbers around using recursive function
#But can only move 1 number at a time
#Bigger number cannot be after smaller number
# def tHanoi(t):
#     if len(list1)==0:
#         return list3.append(list1[0])
#     else:
#         for i in list1:
#             if i in list2 and i<list2[]:


