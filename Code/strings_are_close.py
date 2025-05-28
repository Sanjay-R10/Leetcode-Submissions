from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1) != set(word2):
            return False
        
        frequence1 = Counter(word1)
        frequence2 = Counter(word2)

        return sorted(frequence1.values()) == sorted(frequence2.values())