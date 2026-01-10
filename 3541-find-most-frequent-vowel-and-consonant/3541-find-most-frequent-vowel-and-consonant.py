class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel = {}
        conso = {}
        for i in s:
            if i in ['a','e','i','o','u']:
                vowel[i] = vowel.get(i,0) + 1
            else:
                conso[i] = conso.get(i,0) + 1
                
        max_vowel = max(vowel.values()) if vowel else 0
        max_conso = max(conso.values()) if conso else 0
        return max_vowel + max_conso