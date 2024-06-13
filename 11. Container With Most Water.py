class Solution:
    def maxArea0(self, height: list[int]) -> int:
        a = 0
        for i,hl in enumerate(height) :
            for j,hr in enumerate(height[i+1:]) :
                anew = min(hl, hr) * (j+1)
                a = max(a, anew)
        return a
    def maxArea(self, height: list[int]) -> int:
        a = 0
        i,j = 0, len(height)-1
        while i<j :
            hl = height[i]
            hr = height[j]
            a = max(a, min(hl, hr) * (j-i))
            if hl<hr :
                i += 1
            else:
                j += -1
        return a



print(f'answer = {Solution().maxArea(height = [1,8,6,2,5,4,8,3,7])}')
print(f'answer = {Solution().maxArea(height = [1,1])}')