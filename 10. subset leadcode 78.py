# we have 2 choices
# [a, b, c]
# include index i or not include it
# for multiple choices diagram will form a tree


sub = []
def subsets(l, index=0, path=[]):
    if index==len(l):
        sub.append(path[:])
        return

    subsets(l, index+1, path)
    path.append(l[index])
    subsets(l, index+1, path)
    path.pop()

subsets(['a', 'b', 'c'])
print(sub)