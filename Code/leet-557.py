class Solution:
    def reverseWords(self, s: str) -> str:
        result = []
        word = []

        for char in s :
            if char != " ":
                word.append(char)
            else:
                word.reverse()
                result.extend(word)
                result.append(" ")
                word = []
        word.reverse()
        result.extend(word)

        return ''.join(result)