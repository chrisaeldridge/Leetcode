import timeit
from itertools import chain

def f1(l, numRows):
    for i in range(numRows):
        l[i] = ''.join(l[i])
    l = ''.join(l)
    return l

def f2(l):
    l = ''.join([ x for xs in l for x in xs])
    return l

def f3(l):
    l = ''.join(list(chain.from_iterable(l)))
    return l

numRows = 3
l = [['a','2'],['b','1','3'],['c','4']]

print(f1(l,numRows))
print(f2(l))
print(f3(l))

if __name__ == "__main__":
    print(timeit.timeit('f1(l,numRows)',"from __main__ import f1, numRows, l",number=10000))
    print(timeit.timeit('f2(l)',"from __main__ import f2, l",number=10000))
    print(timeit.timeit('f3(l)',"from __main__ import f3, l",number=10000))
