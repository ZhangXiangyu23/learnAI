class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        i = 0
        row_list = []
        column_list = []
        while (i < len(matrix)):
            j = 0
            while (j < len(matrix[0])):
                if matrix[i][j] == 0:
                    row_list.append(i)
                    column_list.append(j)
                j += 1
            i += 1

        # 对行进行置0
        x = 0
        while (x < len(row_list)):
            j = 0  # 这里特别注意
            while (j < len(matrix[0])):
                matrix[row_list[x]][j] = 0
                j += 1
            x += 1
        # 对列进行置0
        y = 0
        while (y < len(column_list)):
            i = 0  # 这里特别注意
            while (i < len(matrix)):
                matrix[i][column_list[y]] = 0
                i += 1
            y += 1



if __name__ == "__main__":
    s = Solution()
    mm = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    s.setZeroes(mm)
    print(mm)