
def one_to_N(n):
    if n==0: return

    one_to_N(n-1)
    print(n, end=" ")

def range_print(start, end):
    # both end points are inclusive
    if start>end: return
    # end point is not included
    # if start==end: return

    print(start, end=" ")
    range_print(start+1, end)

one_to_N(5)
print()
range_print(6, 10)