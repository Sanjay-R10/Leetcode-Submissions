class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count = Counter(chars)
        total = 0

        for word in words :
            word_count = Counter(word)
            if all(word_count[c] <= char_count.get(c,0) for c in word):
                total += len(word)
        return total
