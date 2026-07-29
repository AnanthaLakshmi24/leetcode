class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum = 0 
        for i in range(k):
            sum += nums[i]
        maxAvg = float(sum/k)
        n = len(nums)
        end = k
        start = 1
        while (end<n):
            sum += nums[end]-nums[start-1]
            avg = float(sum/k)
            maxAvg = max(avg,maxAvg)
            end +=1
            start +=1
        return maxAvg