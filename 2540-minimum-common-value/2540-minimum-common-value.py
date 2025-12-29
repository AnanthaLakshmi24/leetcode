class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # common = set(nums1).intersection(set(nums2))
        # if len(common)>0:
        #     return min(common)
        # else:
        #     return -1
        set1= set(nums1)
        for x in nums2:
            if x in set1:
               return x
        return -1