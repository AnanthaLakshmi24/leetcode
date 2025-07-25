class Solution(object):
    def alternateDigitSum(self, n):
        sum0=0
        sum1=0
        count=0
        while n != 0:
            if count % 2 == 0:
                sum0 += n % 10
            else:
                sum1 += n % 10
            n //= 10
            count += 1
        if count % 2 == 0:
            return (sum1 - sum0) 
        else:
            return (sum0 - sum1)