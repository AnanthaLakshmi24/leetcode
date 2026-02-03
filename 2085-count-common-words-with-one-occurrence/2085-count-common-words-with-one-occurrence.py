class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        counter1 = Counter(words1)
        counter2 = Counter(words2)
        val = 0
        for key in counter1:
            if counter1[key] == 1 and counter2[key] == 1:
                val += 1
        return val