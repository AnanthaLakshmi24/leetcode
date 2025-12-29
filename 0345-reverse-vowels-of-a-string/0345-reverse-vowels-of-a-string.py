class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'A','E','I','O','U','a','e','i','o','u'}
        l = list(s)
        i,j = 0,len(l)-1
        while i<j:
            if l[i] in vowels:
                if l[j] in vowels:
                    l[i],l[j] = l[j],l[i]
                    i += 1
                    j -= 1
                else:
                    j -=1
            else:
                i += 1

        return ''.join(l)
        