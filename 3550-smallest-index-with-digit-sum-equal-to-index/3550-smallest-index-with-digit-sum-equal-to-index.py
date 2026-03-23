class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        li=[]
        for i in nums:
            li.append(sum(list(map(int,str(i)))))
        for i in range(len(li)):
            if i == li[i]:
                return i
                break
        return -1