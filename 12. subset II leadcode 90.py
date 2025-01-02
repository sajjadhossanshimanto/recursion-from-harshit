

# include - non include
all_sub = []
def subsets2(l, index=0, path=[]):
    '''sorting is must before passing to the function'''

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
        

l = ['a', 'b', 'b', 'c']
s.sort()
subsets2(l)
print(all_sub)
