

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # init left and right pointers
        left = 0
        right = len(numbers)-1
        
        # loop as long as the left pointer remains less than the right pointer
        while left < right :
            sum = numbers[left] + numbers[right]
            if sum > target :
                right += -1 # sum too big, move the right inward
            elif sum < target:
                left += 1 # sum too big, move the left inward
            else :
                break # we found the indices
        # they want the indices to start at 1 in this problem
        return [left+1,right+1]

print(f'answer = {Solution().twoSum([-3,-2,-1,0,2,3,9], 3)}') #answer should be [4,6]
print(f'answer = {Solution().twoSum([2,7,11,15], 9)}') #answer should be [1,2]
print(f'answer = {Solution().twoSum([2,3,4], 6)}') #answer should be [1,3]
print(f'answer = {Solution().twoSum([-1,0], -1)}') #answer should be [1,2]