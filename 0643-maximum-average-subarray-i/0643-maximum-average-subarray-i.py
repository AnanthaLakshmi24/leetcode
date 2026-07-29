class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = sum(nums[:k])
        maxAvg = float(curr_sum/k)
        n = len(nums)
        end = k
        start = 1
        while (end<n):
            curr_sum += nums[end]-nums[start-1]
            avg = float(curr_sum/k)
            maxAvg = max(avg,maxAvg)
            end +=1
            start +=1
        return maxAvg