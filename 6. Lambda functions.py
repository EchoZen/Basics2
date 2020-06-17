# Lambda expressions= anonymous functions
g= lambda x: x+2 # lambda input: output/return value

# More than 1 input use comma

list=[(9,0),(8,4),(7,2),(10,5),(32,53)]
list.sort(key=lambda x:x[1], reverse=True) # sorting by 2nd tuple
print(list)