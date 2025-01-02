# we have 2 choices
# [a, b, c]
# include index i or not include it
# for multiple choices diagram will form a tree

# this is called pick and not pick method


sub = []
def subsets(l, index=0, path=[]):
    if index==len(l):
        sub.append(path[:])
        return

    subsets(l, index+1, path)
    path.append(l[index])
    subsets(l, index+1, path)
    path.pop()


# dp approch for generating sub sets
# time complexity is the same
# but offer a better space complexity of 2^n instade of n.2^n
def subsets2(l):
    sub = [[]]
    for ele in l:
        for j in range(len(sub)):# trick to overcome sub[:]
            sub.append(sub[j]+[ele])
    
    return sub


subsets(['a', 'b', 'c'])
print(sub)
print(subsets2(['a', 'b', 'c']))