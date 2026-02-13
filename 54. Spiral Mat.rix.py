class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row_len=len(matrix)
        col_len=len(matrix[0])

        first_row=0
        first_col=0
        last_row=row_len-1
        last_col=col_len-1

        res=[]
        

        while first_row <= last_row and first_col <= last_col:
            
            for col in range(first_col,last_col+1):
                res.append(matrix[first_row][col])
            first_row += 1

            for row in range(first_row,last_row+1):
                res.append(matrix[row][last_col])
            last_col -= 1

            if first_row <= last_row:
                for col in range(last_col,first_col-1,-1):
                    res.append(matrix[last_row][col])
            
                last_row -= 1

            if first_col <= last_col:
                for row in range(last_row,first_row-1,-1):
                    res.append(matrix[row][first_col])
                
                first_col += 1
            
        return res
                        

                    
