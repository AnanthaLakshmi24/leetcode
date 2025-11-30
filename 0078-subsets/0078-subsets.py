class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res =[]
        def f(i,curr):
            if (i>=len(nums)):
                res.append(curr.copy())
                return
            curr.append(nums[i])
            f(i+1,curr)
            curr.pop()
            f(i+1,curr)
        f(0,[])
        return res