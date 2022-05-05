class Solution:
    def check_3py3 (self,window) -> bool:
        freq={}
        for i in range(9):
            if window[i//3][i%3] == ".": continue
            if window[i//3][i%3] in freq:
                return False
            else:
                freq[window[i//3][i%3]] = 1
        return True

    def check_row(self, row) -> bool:
        freq={}
        for i in row:
            if i == ".": continue
            if i in freq:
                return False
            else:
                freq[i] = 1
        return True


    def isValidSudoku(self, board) -> bool:
        cols=[{},{},{},{},{},{},{},{},{}]
        for i in range(0,9):
            if not self.check_row(board[i]):
                return False
            for j in range(0,9):
                if j%3 == 0 and i%3 == 0:
                    sublist=[]
                    for x in range(i, i+3):
                        sublist.append(board[x][j:j+3])
                    if not self.check_3py3(sublist):
                        return False
                if board[i][j] == ".": continue
                if board[i][j] in cols[j]:
                    return False
                else:
                    cols[j][board[i][j]] = 1
        return True


obj=Solution()
board=[
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
    ]
print(obj.isValidSudoku(board))
