class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        row_len=len(image)
        col_len=len(image[0])

        for row in range(row_len):
            image[row].reverse()
            for col in range(col_len):
                if image[row][col] == 0:
                    image[row][col] = 1
                else:
                    image[row][col] = 0

        return image
