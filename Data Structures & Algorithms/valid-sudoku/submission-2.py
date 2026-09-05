class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            row_set = set() # hor
            col_set = set() # vert
            subgrid_set = set() # subgrid

            for col in range(9):
                x =  board[row][col]
                y =  board[col][row]
                zx, zy = ( (row*3) + (col//3) )%9, ( (row//3)*3 + (col%3) )%9
                z = board[zx][zy]
                if x != '.':
                    if x in row_set: return False
                    row_set.add(x)
                if y != '.':
                    if y in col_set: return False
                    col_set.add(y)
                if z != '.':
                    if z in subgrid_set: return False
                    subgrid_set.add(z)
        return True
