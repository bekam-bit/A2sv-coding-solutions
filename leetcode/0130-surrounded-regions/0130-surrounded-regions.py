class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

        def inbound(row, col):
            return (0 <= row < len(board) and 0 <= col < len(board[0]))
        
        def dfs(row, col):
            if not inbound(row, col) or board[row][col] != "O" or visited[row][col]:
                return
            
            visited[row][col] = True

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for i in range(len(board)):
            if board[i][0] == "O" and not visited[i][0]:
                dfs(i, 0)

            if board[i][len(board[0]) - 1] == "O" and not visited[i][len(board[0]) - 1]:
                dfs(i, len(board[0]) - 1)
        
        for j in range(len(board[0])):
            if board[0][j] == "O" and not visited[0][j]:
                dfs(0, j)

            if board[len(board) - 1][j] == "O" and not visited[len(board) - 1][j]:
                dfs(len(board) - 1, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and not visited[i][j]:
                    board[i][j] = "X"
            


                
 
                            
                            

                

                    

        