l = [[]]
print(l)

l[0].append('a')
print(l)

l.append('b')
print(l)
print(l[0])
print(l[1])


print("===============")
l = [[] for i in range(4)]
print(l)
l[0].append('a')
l[1].append('b')
l[1].append('b2')
print(l)

print("===============")
l = list("abc123")
print(l)
l[0] = '3'
l[5] =  'a'
print(l)