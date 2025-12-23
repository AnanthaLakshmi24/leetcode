class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        # e = 0
        # od = 0
        # for i in range(len(nums)):
        #     if i%2==0:
        #         e += nums[i]
        #     else:
        #         od += nums[i]
        # return e-od/
        s=0
        for i in range(len(nums)):
            if(i%2==0):
                s+=nums[i]
            else:
                s-=nums[i]
        return s