

# with for loop
all_sub = []
def subsets1(l, index=0, temp = []):
    
    all_sub.append(temp[:])
    for i in range(index, len(l)):
        temp.append(l[i])
        subsets1(l, i+1, temp)
        temp.pop()


# include - non include
all_sub = []
def subsets2(l, index=0, path=[]):
    if index >= len(l):
        all_sub.append(path[:])
        return 
    
    # include
    path.append(l[index])
    subsets2(l, index+1, path)
    path.pop()

    # not include
    # while i is indexible and  `cur char` == `next char`
    while index<len(l)-1 and l[index]==l[index+1]:
        # if 
        #     break
        index+=1
    
    if index<len(l):
        subsets2(l, index+1, path)
        

subsets2(['a', 'b', 'b', 'c'])
print(all_sub)
