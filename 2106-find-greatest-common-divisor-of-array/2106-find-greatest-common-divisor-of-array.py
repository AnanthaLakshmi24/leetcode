import math
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        return gcd(nums[-1],nums[0])