# import numpy as np
import timeit
class Solution:
    def reverse(self, x: int) -> int:
        
        # get the sign
        sign = 1 if x>=0 else -1
        
        # convert the integer to a reversed string
        revint = int(str(abs(x))[::-1]) * sign
        
        # convert the original integer to a string
        origintstr = str(x)

        # re-reverse the reversed string so we can check it matches the original string; if not we had an over/underflow
        rerevint = str(abs(revint))[::-1]
        if sign < 0:
            rerevint = '-' + rerevint
        i = len(origintstr) - 1
        while origintstr[i] == '0' and i>=0:
            rerevint = rerevint + '0'
            i -= 1
        
        
        # if over/underflow return zero
        if revint > (2**31)-1 or revint < -2**31 or rerevint!=origintstr:
            return 0
        else :
            return revint
        
    def reverse2(self, x: int) -> int:
        rev = 0
        sign = 1 if x>=0 else -1
        x = abs(x)
        while x != 0:
            digit = x % 10
            rev = rev * 10 + digit
            x //= 10
            dummy = 1
        rev *= sign
        
        if rev > 2**31 - 1 or rev < -2**31:
            return 0
        
        return rev
        
print(f'answer = {Solution().reverse(x= -1000)}')
print(f'answer = {Solution().reverse2(x= -1000)}')

n = -1000
if __name__ == "__main__":
    print(timeit.timeit('Solution().reverse(n)',"from __main__ import Solution, n",number=10000))
    print(timeit.timeit('Solution().reverse2(n)',"from __main__ import Solution, n",number=10000))