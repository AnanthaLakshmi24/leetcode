class Solution:
    def averageValue(self, nums: List[int]) -> int:
        avg=0
        c=0
        for num in nums:
            if num%2==0 and num%3==0:
                avg=avg+num
                c=c+1
        if c>0:
            return avg//c
        else:
            return 0
        