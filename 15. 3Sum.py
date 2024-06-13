class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # sort the list
        nums.sort()
        # init list of lists
        tuplist = []  # stores: {val : index}
        # loop through the numbers
        for left, n in enumerate(nums):
            # it's sorted so if we start with a positive mumber we'll never find a set
            if n > 0 :
                break    
            
            # skip if same as last time, since it would result in duplicate list
            if left>0 and n==nums[left-1]:
                continue
            
            # init mid and right pointers
            mid = left+1
            right = len(nums)-1
            
            # loop as long as the mid pointer remains less than the right pointer
            while mid < right :
                sum = n + nums[mid] + nums[right]
                if sum > 0 :
                    right += -1 # sum too big, move the right inward
                elif sum < 0:
                    mid += 1 # sum too big, move the left inward
                else :
                    tuplist.append([n, nums[mid], nums[right]]) # we found the indices, append the list
                    mid += 1 # move the mid pointer in
                    # increment the mid pointer again when it's the same as last time
                    while mid < right and nums[mid]==nums[mid-1] :
                        mid += 1
        
        return tuplist

print(f'answer = {Solution().threeSum([-3,-2,-1,0,2,3,9])}') #answer should be [-3,0,3],[-2,0,2]
print(f'answer = {Solution().threeSum([2,7,11,15, -1, -1])}') #answer should be [2, -1, -1]
print(f'answer = {Solution().threeSum([2,3,4])}') #answer should be []
print(f'answer = {Solution().threeSum([-1,0,1])}') #answer should be [-1,0,1]