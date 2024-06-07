from collections import deque

class Solution:
    def lengthOfLongestAlphabeticalSubstring(self, s: str) -> int:
        maxlen = 0
        q = deque()
        qlong = deque()
        for c in s:
            if len(q)>0:
                if not ord(c) in (ord(q[-1]),ord(q[-1])+1):
                    q = deque()
            q.append(c)
            maxlen = max(maxlen, len(q))
            qlong = deque(q) if len(q)>len(qlong) else qlong
        print(qlong)
        return maxlen
    
    def lengthOfLongestAlphabeticalSubstring0(self, s: str) -> int:
        start = 0
        cur_len = 1
        max_len = 1
        for i in range(1,len(s)):
            if ord(s[i]) in (ord(s[i-1]), ord(s[i-1])+1):
                cur_len += 1
            else:
                if cur_len > max_len:
                    max_len = cur_len
                    start = i - cur_len
                cur_len = 1
        if cur_len > max_len:
            max_len = cur_len
            start = len(s) - cur_len
        print(s[start:start+max_len])
        return max_len
    
print(f'answer = {Solution().lengthOfLongestAlphabeticalSubstring("abcabcbb")}')
print(f'answer = {Solution().lengthOfLongestAlphabeticalSubstring("bbbbb")}')
print(f'answer = {Solution().lengthOfLongestAlphabeticalSubstring("")}')
print(f'answer = {Solution().lengthOfLongestAlphabeticalSubstring("xyz")}')
print(f'answer = {Solution().lengthOfLongestAlphabeticalSubstring("abcaaaaa")}')