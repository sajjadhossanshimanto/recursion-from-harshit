

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
    if index == len(l):
        all_sub.append(path[:])
        return 

    # not include
    subsets(l, index+1, path)
    
    # include
    path.append(l[i])
    subsets2(l, index+1, path)
    path.pop()

subsets1(['a', 'b', 'b', 'c'])
print(all_sub)
