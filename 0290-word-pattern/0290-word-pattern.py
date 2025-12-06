class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(words) != len(pattern):
            return False
        hashmap1 = {}
        hashmap2 = {}
        for idx, letter in enumerate(pattern):
            if letter not in hashmap1 and words[idx] not in hashmap2:
                hashmap1[letter] = words[idx]
                hashmap2[words[idx]] = letter
            elif hashmap1.get(letter) != words[idx] or hashmap2.get(words[idx]) != letter:
                return False
        return True
        