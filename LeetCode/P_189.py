# coding:utf-8

class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = []
        # 指向列表中的最后一个元素
        i = len(nums) - 1
        count = 0
        # 这一步相当关键，是为了避免k大于列表长度
        k =  k % len(nums)
        while (True):
            if count == k:
                break
            temp.append(nums[i])
            i -= 1
            count += 1


        # 将剩下的元素,向右移动k个位置
        while(i >= 0):
            nums[i + k] = nums[i]
            i -= 1

        # 将之前temp的元素倒序全部放到nums的最前面
        j = len(temp) - 1
        k = 0
        while (j >= 0):
            nums[k] = temp[j]
            k += 1
            j -= 1



