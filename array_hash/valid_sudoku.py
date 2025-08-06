class Solution(object):
    def isValidSudoku(self, board):
        seen = set()

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue

            # cria chaves únicas para linha, coluna e 3x3
                row_key = ('row',i, num)
                col_key = ('col',j, num)
                box_key = ('box',i // 3, j // 3, num)

            
                if row_key in seen or col_key in seen or box_key in seen:
                    return False

            
                seen.update([row_key, col_key, box_key])

        return True
        