class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = ['a','e','i','o','u']
        c = 0

        for i in range(k):
            if s[i] in vowel:
                c+=1
        max_c = c

        for i in range(k,len(s)):
            if s[i] in vowel:
                c+=1
            if s[i-k] in vowel:
                c-=1
            max_c = max(max_c,c)

        return max_c