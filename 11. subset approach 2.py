# here we will think -> with which element can we form different subsets


all_subs = []
def subsets(l, index=0, temp=[]):
    # if index>len(l):
    #     return

    all_subs.append(temp[:])
    for i in range(index, len(l)):
        temp.append(l[i])
        subsets(l, i+1, temp)
        temp.pop()

subsets(["a", 'b', 'c'])
print(all_subs)