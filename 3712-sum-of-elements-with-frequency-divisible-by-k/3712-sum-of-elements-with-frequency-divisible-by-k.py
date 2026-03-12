class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        ans=0
        freq_nums=Counter(nums)
        for key,value in freq_nums.items():
            if value % k==0:
                ans+=(key*value)
        return ans