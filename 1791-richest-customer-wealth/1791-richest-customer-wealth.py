class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans=0
        for n in accounts:
            ans=max(ans,sum(n))
        return ans
