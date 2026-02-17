from collections import defaultdict

class Solution:
    def validSudoku(self, board):
        row = defaultdict(set)
        col = defaultdict(set)
        sqr = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                elif (board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in sqr[(r//3,c//3)]):
                    return False
                col[c].add(board[r][c])
                row[r].add(board[r][c])
                sqr[(r//3, c//3)].add(board[r][c])
        return True

board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

s = Solution()

print(s.validSudoku(board))



# Here the time and space complexity is O(1). Since the Sudoku board is always 9×9 (81 cells fixed), the algorithm always performs exactly 81 iterations. Even though there are nested loops, the number of operations is constant regardless of input size. Since the board size is fixed at 9×9, the space used is constant and doesn't grow with input.