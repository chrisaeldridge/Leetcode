from heapq import merge

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        mergedlist = list(merge(nums1,nums2))
        print(mergedlist)
        mididx = len(mergedlist) // 2
        median = (mergedlist[mididx] + mergedlist[~mididx]) / 2
        return median


print(f'answer = {Solution().findMedianSortedArrays([1,2,4],[99])}')
