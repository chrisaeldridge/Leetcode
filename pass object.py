def f(a,b) :
    a.append(b)
    
a = list()
f(a,1)
f(a,2)
print(a)

s = 'abc123'
for i in range(0,10) :
    # c = i<len(s) and s[i].isalpha()
    print(s[i] if i<len(s) else '')