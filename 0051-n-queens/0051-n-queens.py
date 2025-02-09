class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def placeQueen(row):
            if row == n:
                # Convert the board to the required output format and store the solution
                sol.append(["".join(r) for r in board])
                return
            
            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                
                # Place the queen
                board[row][col] = 'Q'
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                
                # Recur to place the next queen
                placeQueen(row + 1)
                
                # Backtrack
                board[row][col] = '.'
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
        
        # Initialise variables
        board = [['.'] * n for _ in range(n)]
        sol = []
        cols = set()      # Columns under attack
        diag1 = set()     # Diagonals under attack
        diag2 = set()     # Anti-diagonals under attack
        
        placeQueen(0)
        return sol
        