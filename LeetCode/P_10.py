# coding:utf-8

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)

        # 匹配函数
        def matches(i, j):
            if i == 0:
                return False
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]

        # 进行初始化
        f = [[False] * (n + 1) for _ in range(m + 1)]
        # 两个空字符串是可以匹配的
        f[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                # p[j-1]为*时
                if p[j - 1] == '*':
                    f[i][j] |= f[i][j - 2]
                    if matches(i, j - 1):
                        f[i][j] |= f[i - 1][j]
                # 如果p[j-1]不是*的话，如果这一位s和p能匹配的上
                # 取决于两个字符串前面的部分
                else:
                    if matches(i, j):
                        f[i][j] |= f[i - 1][j - 1]
        # 返回结果
        return f[m][n]


if __name__ == "__main__":
    s = "aa"
    p = "a*"
    x = Solution()
    print(x.isMatch(s, p))