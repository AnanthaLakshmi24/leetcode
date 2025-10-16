class Solution:
    def longestPalindrome(self, s: str) -> str:
        c =""
        n = len(s)
        for i in range(n):
            for j in range(i,n):
                substring = s[i : j+1]
                if substring == substring[::-1]: 
                    if len(substring)>len(c):
                        c=substring
        return c 