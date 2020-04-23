#Binary Trees: one parent node can only have maximum 2 child nodes (only 2 outcomes MAX)
#Binary Trees is a form of recursion
#Complete Binary Tree has 2 child nodes

tree= [[[7],8,[9]],5,[[1],2,[3]]]

def numOfNodes(t):
    if len(t)==1:
        return 1
    else:
        numLeft= numOfNodes(t[0])
        numRight= numOfNodes(t[2])
        return numLeft+numRight+1

print(numOfNodes(tree))

def sumOfNodes(t):
    if len(t)==1:
        return t[0]
    else:
        leftSum= sumOfNodes(t[0])
        rightSum= sumOfNodes(t[2])
        return t[1]+ leftSum+rightSum

print(sumOfNodes(tree))

def maxNode(t):
    if len(t)==1:
        return t[0]
    else:
        maxValue= t[1]
        leftMax= maxNode(t[0])
        rightMax= maxNode(t[2])
        if leftMax>maxValue:
            maxValue= leftMax
        if rightMax>maxValue:
            maxValue= rightMax
        return maxValue
print(maxNode(tree))

def minNodes(t):
    if len(t)==1:
        return t[0]
    else:
        leftMin= minNodes(t[0])
        rightMin= minNodes(t[2])
        minValue= t[1]
        if leftMin<minValue:
            minValue= leftMin
        if rightMin<minValue:
            minValue= rightMin
        return minValue

print(minNodes(tree))

def mirror(t):
    if len(t)==1:
        return t[0]
    else:
        parent=t[1]
        mirrorLtree= mirror(t[0])
        mirrorRtree= mirror(t[2])
        return [[mirrorRtree], parent, [mirrorLtree]]
print(mirror(tree))

#Print CBT

tree= [[[1],2,[3]],4,[[5],6,[7]]]
def printTree(t, level):
    if len(t)==1:
        print(""*level, end="")
        print(t[0])
    else:
        printTree(t[2],level+1)
        print(" "*level,end="")
        print(t[1])
        printTree(t[0],level+1)

printTree(tree, 4)
