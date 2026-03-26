class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s = 0
        p =1
        temp = n
        while(n>0):
            rem = n%10
            s += rem
            p *= rem
            n //= 10
        return temp %(s+p)==0