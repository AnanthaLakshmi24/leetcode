class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # curr_sum = sum(nums[:k])
        # maxAvg = float(curr_sum/k)
        # n = len(nums)
        # end = k
        # start = 1
        # while (end<n):
        #     curr_sum += nums[end]-nums[start-1]
        #     avg = float(curr_sum/k)
        #     maxAvg = max(avg,maxAvg)
        #     end +=1
        #     start +=1
        # return maxAvg

        curr_sum = sum(nums[:k])
        max_sum = curr_sum

        for i in range(k,len(nums)):
            curr_sum =curr_sum+nums[i]-nums[i-k]
            max_sum = max(curr_sum,max_sum)
        return max_sum/k