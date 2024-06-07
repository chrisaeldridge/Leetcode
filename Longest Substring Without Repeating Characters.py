from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        q = deque()
        qlong = deque()
        for c in s:
            if c in q:
                while q.popleft() != c:
                    pass
            q.append(c)
            maxlen = max(maxlen, len(q))
            qlong = deque(q) if len(q)>len(qlong) else qlong
        print(qlong)
        return maxlen
        
print(f'answer = {Solution().lengthOfLongestSubstring("abcabcbb")}')
print(f'answer = {Solution().lengthOfLongestSubstring("bbbbb")}')
print(f'answer = {Solution().lengthOfLongestSubstring("pwwkew")}')
print(f'answer = {Solution().lengthOfLongestSubstring("dvdf")}')
print(f'answer = {Solution().lengthOfLongestSubstring("")}')