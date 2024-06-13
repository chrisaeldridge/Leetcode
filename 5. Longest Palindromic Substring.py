from collections import deque

class Solution:
    def find_palindromes(s: str, j, k):
        palindromes = []
        while j >= 0 and k < len(s) and s[j] == s[k]:
            #each outward expansion is its own palindrome
            palindromes.append(s[j: k + 1])
            j -= 1
            k += 1
        return palindromes
    
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0 :
            return ''
        if len(s) == 1 :
            return s

        palindromes = []
        for i in range(len(s)):
            # search for odd length starting from center index
            palindromes += Solution.find_palindromes(s, i - 1, i + 1)
            # search for even length index starting from current index plus the char to the right
            palindromes += Solution.find_palindromes(s, i, i+1)     
        if not len(palindromes)>0 :
            palindromes += s[0] #if we didnt find any palindromes just return the first character of the string
        return max(palindromes, key=len)
        
print(f'answer = {Solution().longestPalindrome("abcabadabbcbb")}')
print(f'answer = {Solution().longestPalindrome("a")}')
print(f'answer = {Solution().longestPalindrome("ac")}')