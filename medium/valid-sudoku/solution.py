class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            numbers = [cell for cell in row if cell.isdigit()]
            if len(set(numbers)) != len(numbers):
                return False
        for col in range(len(board[0])):
            numbers = [board[row][col] for row in range(len(board)) if board[row][col].isdigit()]
            if len(set(numbers)) != len(numbers):
                return False
        for startRow in range(0, 9, 3):
            for startCol in range(0, 9, 3):
                numbers = []
                for i in range(3):
                    for j in range(3):
                        cell = board[startRow + i][startCol + j]
                        if cell.isdigit():
                            numbers.append(cell)
                if len(set(numbers)) != len(numbers):
                    return False


        return True
        
