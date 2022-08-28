class Solution:
    def matrixReshape(self, mat, r: int, c: int):
        # 原矩阵行数
        m = len(mat)
        # 原矩阵列数
        n = len(mat[0])
        if (m * n) != (r * c):
            return mat
        else:
            i = 0
            j = 0
            outer_mat = []
            inner_mat = []
            while (i < m):
                j = 0
                while (j < n):
                    inner_mat.append(mat[i][j])
                    if len(inner_mat) == c:
                        outer_mat.append(inner_mat)
                        inner_mat = []
                    j += 1
                i += 1

            return outer_mat


if __name__ == "__main__":
    s = Solution()
    print(s.matrixReshape([[1, 2], [3, 4]], r=1, c=4))
