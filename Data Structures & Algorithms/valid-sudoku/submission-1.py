class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Boolean Arrays
        row = [[False] * 9 for _ in range(9)]
        col = [[False] * 9 for _ in range(9)]
        sub = [[False] * 9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                val = board[i][j]

                if val == '.':
                    continue
                ival = int(val) - 1

                sub_box = (i // 3) * 3 + (j // 3)

                if (row[i][ival] or
                    col[j][ival] or
                    sub[sub_box][ival]):
                    return False
                
                row[i][ival] = True
                col[j][ival] = True
                sub[sub_box][ival] = True

        return True
            