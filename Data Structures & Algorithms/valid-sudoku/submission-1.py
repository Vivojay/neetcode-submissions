class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            row_set = set() # hor
            col_set = set() # vert
            subgrid_set = set() # subgrid

            print(f'row = {row}')
            for col in range(9):
                x =  board[row][col]
                y =  board[col][row]
                zx, zy = ( (row*3) + (col//3) )%9, ( (row//3)*3 + (col%3) )%9
                z = board[zx][zy]
                # print(row_set, col_set, subgrid_set)
                # print('::', row, col, zx, zy) #, board[zx][0])
                # print(x, y, z)
                if x != '.':
                    if x in row_set: return False
                    row_set.add(x)
                if y != '.':
                    if y in col_set: return False
                    col_set.add(y)
                if z != '.':
                    if z in subgrid_set: return False
                    subgrid_set.add(z)
                # print()
            print(row_set, col_set, subgrid_set)
            print()

        # print(x, y)
        return True


# loop: (i < 7; j < 7)
        #    [(0, 1), (0, 2), ..., (0, 9)]
        #    [(0, 1), (0, 2), ..., (0, 9)]

