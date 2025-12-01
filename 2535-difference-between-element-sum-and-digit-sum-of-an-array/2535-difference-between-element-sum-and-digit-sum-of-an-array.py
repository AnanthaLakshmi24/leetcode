class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        ele =0
        dig = 0
        for i in nums:
            ele = ele+i
            while i>0:
                rem=i%10
                dig += rem
                i=i//10
        return abs(ele-dig)