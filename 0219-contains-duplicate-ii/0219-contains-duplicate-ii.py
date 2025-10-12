class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        freq={}
        for index,num in enumerate(nums):
            if num in freq and (index-freq[num])<=k:
                return True
            else:
                freq[num]=index
        return False