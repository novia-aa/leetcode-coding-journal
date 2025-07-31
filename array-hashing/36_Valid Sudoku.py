class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows and columns
        for i in range(9):
            row_set = set()
            col_set = set()
            for j in range(9):
                # Row check
                if board[i][j] != '.':
                    if board[i][j] in row_set:
                        return False
                    row_set.add(board[i][j])
                
                # Column check
                if board[j][i] != '.':
                    if board[j][i] in col_set:
                        return False
                    col_set.add(board[j][i])
        
        # Check 3x3 sub-boxes
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                block_set = set()
                for i in range(3):
                    for j in range(3):
                        val = board[box_row + i][box_col + j]
                        if val != '.':
                            if val in block_set:
                                return False
                            block_set.add(val)
        
        return True
