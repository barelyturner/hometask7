lst1 = [5, 10, 201, 111, 3]


def maxnumrecursive(l):
    for el in lst1:
        if max(lst1) == lst1[0]:
            return max(lst1)
        else:
            lst1.sort(reverse=True)
            maxnumrecursive(l)


print(maxnumrecursive(lst1))
