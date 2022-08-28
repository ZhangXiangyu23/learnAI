class Solution:
    def generate(self, numRows):
        # numRows为1时
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            res = [[1], [1, 1]]
            i = 2
            inner = []
            count = 3
            while(i < numRows):
                # 每次重置j
                j = 1
                # 一行的第一个元素
                inner.append(1)
                # 从第三层开始
                while(j < count-1):
                    inner.append(res[i-1][j-1] + res[i-1][j])
                    j += 1
                # 一行的最后一个元素
                inner.append(1)
                res.append(inner)
                inner = []
                count += 1
                i += 1
            return res


if __name__ == "__main__":
    s = Solution()
    print(s.generate(5))