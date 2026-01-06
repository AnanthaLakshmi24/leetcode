class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words = 0
        for s in sentences:
            cnt = len(s.split(" "))
            max_words = max(max_words, cnt)
        return max_words