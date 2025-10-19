class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # result = []        
        # total = 0          
        # for n in nums:
        #     total += n     
        #     result.append(total)  
        # return result

        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i - 1]
        return nums