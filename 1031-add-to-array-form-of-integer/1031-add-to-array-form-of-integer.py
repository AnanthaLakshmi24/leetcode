import sys
sys.set_int_max_str_digits(100000)
# class Solution:
    # def addToArrayForm(self, num: List[int], k: int) -> List[int]:
    #     ans=""
    #     for n in num:
    #         ans=ans+str(n)
    #     l=int(ans)+k
    #     return [int(d) for d in str(l)] 
class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        l = int("".join(map(str, num))) + k
        return [int(d) for d in str(l)]
