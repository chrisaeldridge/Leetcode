

class Solution:
    def twoSum0(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
            
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}  # stores: {val : index}
        # loop through the numbers
        for i, n in enumerate(nums):
            # get the difference between the current number and the target
            diff = target - n
            # if the difference is in the hashmap already, we have found the pair that equals the target 
            if diff in hashmap:
                #return that hashed index and the current index
                return [hashmap[diff], i]
            # the diff was not in the hashmap; add the current num to the hash and move next
            hashmap[n] = i


print(f'answer = {Solution().twoSum([3,3],6)}')