from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # s = set()
        # d = []
        # for num in nums:
        #     if num not in s:
        #         s.add(num)
        #         d.append(num)   
        # for i in range(len(d)):
        #     nums[i] = d[i]
        
        # return len(d)
        k =1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k=k+1
        return k