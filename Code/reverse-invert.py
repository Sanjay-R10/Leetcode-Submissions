class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            row.reverse()
            for bit in range(len(row)):
                if row[bit] == 0:
                    row[bit] = 1
                else:
                    row[bit] = 0
        return image