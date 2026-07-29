class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        freq={}
        for index,num in enumerate(nums):
            if num in freq and (index-freq[num])<=k:
                return True
            else:
                freq[num]=index
        return False

        # n= len(nums)
        # start = 0
        # seen = set()
        # for end in range(n):
        #     if nums[end] in seen and (end-start)<=k:
        #         return True
            
        #     seen.add(nums[end])

        #     if (end-start) >=k:
        #         seen.remove(nums[start])
        #         start+=1
        # return False
