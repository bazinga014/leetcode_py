from typing import List
from typing import Union

class Mergesort:
    def merge_sort(self, nums: List[int]):
        if len(nums) < 2:
            return
        left, right = 0, len(nums)-1
        self.process(nums, left, right)
    def process(self, nums: List[int], left, right):
        if left == right:
            return
        mid = ((right - left) >> 1) + left
        self.process(nums,left, mid)
        self.process(nums, mid+1, right)
        self.merge(nums, left, mid, right)

    def merge(self, nums: List[int], left: int, mid: int, right: int):
        #辅助数组
        result = []
        i, j = left, mid+1
        while i <= mid and j <= right:
            if nums[i] < nums[j]:
                result.append(nums[i])
                i += 1
            else:
                result.append(nums[j])
                j += 1

        # result.extend(nums[i:mid+1]) # 也可以这么写
        # result.extend(nums[j:right+1])
        while i <= mid:
            result.append(nums[i])
            i += 1
        while j <= right:
            result.append(nums[j])
            j += 1

        for i in range(len(result)):
            # 一定要注意是left+i!!!因为要写回原数组！！！
            nums[left + i] = result[i]

# m = Mergesort()
# arr = [1, 3, 6, 2, 4, 5]
# m.merge_sort(arr)
# print(arr)

class SmallSum:
    def get_small_sum(self, nums: List[int])-> int:
        if len(nums) < 2:
            return 0
        left, right = 0, len(nums)-1
        return self.process(nums, left, right)
    def process(self, nums: List[int], left: int, right: int):
        if left == right:
            return 0
        mid = left + ((right - left) // 2)
        return self.process(nums, left, mid) \
            + self.process(nums, mid+1, right) \
            + self.merge(nums, left, mid, right)


    def merge(self, nums: List[int], left: int, mid: int, right: int):
        help_arr = []
        result = 0

        i, j = left, mid+1
        while i <= mid and j <= right:
            if nums[i] < nums[j]:
                help_arr.append(nums[i])
                result += nums[i] * (right - j + 1)
                i += 1
            else:
                help_arr.append(nums[j])
                j += 1

        while i <= mid:
            help_arr.append(nums[i])
            i += 1

        while j <= right:
            help_arr.append(nums[j])
            j += 1

        for i in range(len(help_arr)):
            nums[left + i] = help_arr[i]

        return result

# s = SmallSum()
# print(s.get_small_sum([1,3,4,2,5]))


class ReversePair:
    def print_reverse_pair(self, nums: List[int]):
        if len(nums) < 2:
            print(None)
        left, right = 0, len(nums)-1
        res = self.process(nums, left, right)
        print(res)
    def process(self, nums: List[int], left: int, right: int) -> List[int]:
        res = []
        if left == right:
            return res
        mid = left + (right - left) // 2
        res.extend(self.process(nums, left, mid))
        res.extend(self.process(nums,mid+1, right))
        res.extend(self. merge(nums, left, mid, right))
        return res

    def merge(self, nums: List[int], left: int, mid: int, right: int):
        help_arr = []
        reversed_pair_arr = []
        i, j = left, mid+1
        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                help_arr.append(nums[i])
                i += 1
            else:
                help_arr.append(nums[j])
                # 该数的所有逆序对都加到结果数组中
                for k in range(i, mid+1):
                    reversed_pair_arr.append((nums[k], nums[j]))
                j += 1

        while i <= mid:
            help_arr.append(nums[i])
            i += 1
        while j <= right:
            help_arr.append(nums[j])
            j += 1

        for i in range(len(help_arr)):
            nums[left+i] = help_arr[i]

        return reversed_pair_arr

#
# r = ReversePair()
# r.print_reverse_pair([3,2,4,5,0])

class Flag1:
    def flag_arr(self, nums:List[int], target: int):
        if len(nums) < 2:
            return
        less_idx = -1
        for i in range(len(nums)):
            if nums[i] <= target:
                less_idx += 1
                nums[less_idx], nums[i] = nums[i], nums[less_idx]


class Flag2:
    def flag_arr(self, nums: List[int], target: int):
        if len(nums) < 2:
            return
        less_idx = -1
        more_idx = len(nums)
        i = 0
        while i < more_idx:
            if nums[i] < target:
                less_idx += 1
                nums[less_idx], nums[i] = nums[i], nums[less_idx]
                i += 1
            elif nums[i] > target:
                more_idx -= 1
                nums[more_idx], nums[i] = nums[i], nums[more_idx]
            else:
                i += 1

# f = Flag2()
# arr = [3,1,2,4,5,2,0]
# f.flag_arr(arr, 2)
# print(arr)

class QuickSortV1:
    def quick_sort_v1(self, nums: List[int]):
        if len(nums) < 2:
            return
        self.quick_sort(nums, 0, len(nums) -1) # 快排需要传入左右

    def quick_sort(self, nums: List[int], left: int, right: int):
        # 一定要注意左右边界的问题！！！
        if left >= right:
            return
        # 根据两色荷兰国旗的思想，找到小于等于target区的less，和大于区的more
        # 对于[3, 5, 2, 6, 4]。左边界为1，右边界为3（形如32|4|56）
        less, more = self.partition(nums, left, right)
        self.quick_sort(nums, left, less)
        self.quick_sort(nums, more, right)

    def partition(self, nums: List[int], left: int, right: int) -> (int, int):
        less = left - 1
        target = nums[right] # target就用最后一个数！
        for i in range(left, right):
            if nums[i] <= target:
                less += 1
                nums[i], nums[less] = nums[less], nums[i]
        nums[less+1], nums[right] = nums[right], nums[less+1] # 这里一定不能用target换。而要写成nums[right]!!!
        more = less + 2 # 大于区一定是less区边界+2，因为target换过来了
        return less, more

# q = QuickSortV1()
# a = [3, 2, 4, 6, 5, 5, 2, 1, 4, 6, 7]
# q.quick_sort_v1(a)
# print(a)

class QuickSortV2:
    def quick_sort_v2(self, nums: List[int]):
        if len(nums) < 2:
            return
        self.quick_sort(nums, 0, len(nums)-1)

    def quick_sort(self, nums: List[int], left: int, right: int):
        # 一定要注意左右边界的问题！！！
        if left >= right:
            return
        less, more = self.partition(nums, left, right)
        self.quick_sort(nums, left, less)
        self.quick_sort(nums, more, right)

    def partition(self, nums: List[int], left: int, right: int) -> (int, int):
        less = left - 1
        more = right + 1
        target = nums[right]
        while left < more:
            if nums[left] < target:
                less += 1
                nums[less], nums[left] = nums[left], nums[less]
                left += 1
            elif nums[left] == target:
                left += 1
            else:
                more -= 1
                nums[more], nums[left] = nums[left], nums[more]
        # 三色荷兰国旗问题后，无需交换！！因为区域已经排好了！！底下这句一定不能加
        # nums[more], nums[right] = nums[right], nums[more]
        return less, more

# q = QuickSortV2()
# a = [3, 2, 4, 6, 5, 5, 2, 1, 4, 6, 7, 4]
# q.quick_sort_v2(a)
# print(a)

import random
class QuickSortV3:
    def quick_sort_v3(self, nums: List[int]):
        if len(nums) < 2:
            return
        self.quick_sort(nums, 0, len(nums)-1)

    def quick_sort(self, nums: List[int], left: int, right: int):
        # 一定要注意左右边界的问题！！！
        if left >= right:
            return
        less, more = self.partition(nums, left, right)
        self.quick_sort(nums, left, less)
        self.quick_sort(nums, more, right)

    def partition(self, nums: List[int], left: int, right: int) -> (int, int):
        less = left - 1
        more = right + 1
        # 随机选择一个元素！
        target = random.choice(nums[left:right])
        while left < more:
            if nums[left] < target:
                less += 1
                nums[less], nums[left] = nums[left], nums[less]
                left += 1
            elif nums[left] == target:
                left += 1
            else:
                more -= 1
                nums[more], nums[left] = nums[left], nums[more]
        # 三色荷兰国旗问题后，无需交换！！因为区域已经排好了！！底下这句一定不能加
        # nums[more], nums[right] = nums[right], nums[more]
        return less, more

# q = QuickSortV3()
# a = [3, 2, 4, 6, 5, 5, 2, 1, 4, 6, 7, 4]
# q.quick_sort_v3(a)
# print(a)