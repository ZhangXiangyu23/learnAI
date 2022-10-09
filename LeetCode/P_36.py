# coding:utf-8


class Solution:
    def isValidSudoku(self, board):
        rows = [[0] * 9 for _ in range(9)]
        cols = [[0] * 9 for _ in range(9)]
        boxs = [[[0] * 9 for m in range(3)] for n in range(3)]
        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c != '.':
                    index = ord(c) - ord('0') - 1
                    rows[i][index] += 1
                    cols[j][index] += 1
                    boxs[i//3][j//3][index] += 1
                    if rows[i][index] > 1 or cols[j][index] > 1 or boxs[i//3][j//3][index] > 1:
                        return False
        return True


if __name__ == "__main__":
    board = []
    s = Solution()
    s.isValidSudoku(board=board)