# coding:utf-8

class Solution:
    def sortedSquares(self, nums):
        length = len(nums)
        new_list = [0] * length
        left = 0
        right = length - 1
        count = length - 1
        while (left <= right):
            if (nums[left] ** 2) >= (nums[right] ** 2):
                new_list[count] = nums[left] ** 2
                count -= 1
                left += 1
            else:
                new_list[count] = nums[right] ** 2
                count -= 1
                right -= 1

        return new_list


if __name__ == "__main__":
    c = Solution()
    nums = [-4, -1, 0, 3, 10]
    new_list = c.sortedSquares(nums=nums)
    print(new_list)

