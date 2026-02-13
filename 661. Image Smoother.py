class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row_len = len(img)
        col_len = len(img[0])
        res = [[0] * col_len for _ in range(row_len)]

        for r in range(row_len):
            for c in range(col_len):
                total_sum = 0
                count = 0
                
               
                for i in range(r - 1, r + 2):
                    for j in range(c - 1, c + 2):
                        
                        if 0 <= i < row_len and 0 <= j < col_len:
                            total_sum += img[i][j]
                            count += 1
                
                res[r][c] = total_sum // count
                
        return res
