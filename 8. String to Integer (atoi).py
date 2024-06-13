import itertools
import re
class Solution:
    def myAtoi0(self, s: str) -> int:
        # whitespaces, -, +, and numbers
        numset = (32,43,45,48,49,50,51,52,53,54,55,56,57)
        
        # grab beginning of set until we see a character that is not a space,-,+,num
        l = list(itertools.takewhile(lambda x: ord(x) in numset, list(s)))
        
        if len(l) == 0 :
            return 0
        
        #-, +, and numbers
        numset = (43,45,48,49,50,51,52,53,54,55,56,57)
        l = ''.join([ x for x in l if ord(x) in numset])
        l = int(''.join([ x for x in l if ord(x) in numset]))
        return l
    def myAtoi(self, s: str) -> int:
        if len(s)==0:
            return 0
        # whitespaces, -, +, and numbers
        numset = (32,43,45,48,49,50,51,52,53,54,55,56,57)
        # grab beginning of set until we see a character that is not a space,-,+,num
        l = list(itertools.takewhile(lambda x: ord(x) in numset, list(s)))      
        if len(l) == 0 :
            return 0
        s = ''.join(l)
        
        # now do a regex search on the first matching string starting at beginning
        g = re.search("^[\s]*([+-]?[0-9]+)",s)
        if g == None :
            return 0
        i = int(g.group(1))
        # if over/underflow round it
        if i > (2**31)-1 :
            return (2**31)-1
        elif i < -2**31 :
            return -2**31
        else :
            return i
        
    # def myAtoi(self, s: str) -> int:
    #     l = []
    #     hitsigns = false
    #     for c in s :
    #         if c == ' ' :
    #             pass
    #         elif c in ('-') :
    #             l.append
    #             hitsigns = true
    #         elif ord(c) in (48,49,50,51,52,53,54,55,56,57) :
    #             l.append
    #         else :
    #             break
    #     if 
            
print(f'answer = {Solution().myAtoi("  -1556c23")}')
print(f'answer = {Solution().myAtoi("+-12")}')
print(f'answer = {Solution().myAtoi("words and 987")}')
print(f'answer = {Solution().myAtoi(" -0-1")}')
print(f'answer = {Solution().myAtoi("")}')
print(f'answer = {Solution().myAtoi(" --+0-1")}')
print(f'answer = {Solution().myAtoi("42")}')
print(f'answer = {Solution().myAtoi("   -042")}')
print(f'answer = {Solution().myAtoi("1337c0d3")}')
