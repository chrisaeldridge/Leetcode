class Solution:
    def isPalindrome(self, x: int) -> bool:
        xl = list(str(x))
        xlr = list(xl)
        xlr.reverse()
        if ''.join(xl) == ''.join(xlr) :
            return True
        else :
            return False
        
print(f'answer = {Solution().isPalindrome(0)}')
