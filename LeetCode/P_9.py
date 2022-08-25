# coding:utf-8

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 输入整数为0时
        if x == 0:
            return True
        # 输入整数为负数时
        elif x < 0:
            return False
        # 输入整数为正数时
        else:
            # 将正整数转为字符串类型
            x_string = str(x)
            i = 0
            l = len(x_string)
            while i <= (l//2):
                # 左右"对称"比较
                if x_string[i] != x_string[l-i-1]:
                    return False
                # 为回文数时的，最终临界条件
                elif i == l//2 and x_string[i] == x_string[l-i-1]:
                    return True
                # 循环i
                else:
                    i = i + 1




if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(10))