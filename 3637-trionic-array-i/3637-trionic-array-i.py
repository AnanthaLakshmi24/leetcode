class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        i = 1
        first , second , third = False , False , False
        while i < len(nums):
            if nums[i] > nums[i-1]:
                i+=1
                first = True
            else:
                break
        print(i)
        
        while i < len(nums):
            if nums[i] < nums[i-1]:
                i+=1
                second = True
            else:
                break
            
        print(i)

        while i < len(nums):
            if nums[i] > nums[i-1]:
                i+=1
                third = True
            else:
                break
        
        if i != len(nums):
            return False
        
        print(first , second , third)
        return first and second and third





