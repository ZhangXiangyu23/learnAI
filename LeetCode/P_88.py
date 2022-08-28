class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            pass
        elif m == 0:
            nums1 = nums2
        else:
            temp = nums1
            # temp指针
            i = 0
            # num2指针
            j = 0
            # num1指针
            k = 0
            # 总长度
            length = m + n
            while(k < length):
                # 剩下num2
                if i == m:
                    while(k < length and j < n):
                        nums1[k] = nums2[j]
                        k += 1
                        j += 1
                    # 结束了
                    break
                # 剩下temp
                if j == n:
                    while(k < length and i < m):
                        nums1[k] = temp[i]
                        k += 1
                        i += 1
                    # 结束
                    break

                if temp[i] <= nums2[j]:
                    nums1[k] = temp[i]
                    k += 1
                    i += 1
                else:
                    nums1[k] = nums2[j]
                    k += 1
                    j += 1


if __name__ == "__main__":
    s = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    s.merge(nums1=nums1, nums2=nums2, m=3, n=3)
    print(nums1)