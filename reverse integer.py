import numpy as np
class Solution:
    def reverse(self, x: int) -> int:
        
        # convert the integer to a reversed string
        revint = int(str(abs(x))[::-1]) * np.sign(x)
        
        # convert the original integer to a string
        origintstr = str(x)

        # re-reverse the reversed string so we can check it matches the original string; if not we had an over/underflow
        rerevint = str(abs(revint))[::-1]
        if np.sign(x) < 0:
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
        
print(f'answer = {Solution().reverse(x= -100)}')
