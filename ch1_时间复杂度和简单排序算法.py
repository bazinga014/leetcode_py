from typing import List
from typing import Union

# 选择排序
class SelectionSort:
    def select_sort(self, arr: List[int]):
        """
        选择排序算法思路：每轮从i到len(arr)中选择一个最小值，放在i位置，然后i++,直到i为len(arr)。
        所以需要两层循环：1.i从0到len(arr)，表示每次确定i位置的数，这样从0-i都是排好的；
        2. 内层循环需要从i到len(arr)选择出这里面最小的数，用来和i位置原来的数做交换。
        :param arr: 源数组
        :return: None
        """
        if arr is None or len(arr) < 2:
            return
        for i in range(len(arr)): # 每次确定i位置的数
            min_index = i
            for j in range(i+1, len(arr)): # 从i+1到len(arr)中找出最小数的index
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i] # 进行交换


class OddTimes:
    def print_odd_times_num2(self, nums: List[int]) -> List[int]:
        """
        :param nums: 源数组
        :return: List[int]
        """
        eor = 0
        for num in nums:
            eor ^= num # eor = a ^ b
        right_one = eor & (-eor)
        a = 0
        for num in nums:
            if num & right_one == 0:
                a ^= num
        b = eor ^ a

        return [a, b]

class SingleNumber:
    def print_single_number(self, nums: List[int]) -> int:
        res = 0 # 结果
        for i in range(32):
            cnt = 0 # 记录每一位的数量
            for num in nums: # 每一位统计所有数字
                cnt += ((num >> i) & 1) # 将num右移i位，然后与1
            if cnt % 3 != 0:# 如果该位模3不为0，则说明是单独那个数的位置不为1。
                if i == 31: #python最高位要特殊处理
                    # 这代表单独的数是负数，例如-2：111...10，需要减掉(1<<31)
                    res -= (1 << i)
                else:
                    res += (1 << i) # 结果加上该位为1，也可以写作res |= ((cnt % 3) << i)
        return res


class InsertSort:
    def insert_sort(self, nums: List[int]):
        if nums is None or len(nums) < 2:
            return
        for i in range(1, len(nums)):
            for j in range(i-1, -1, -1): # 从i-1到0遍历
                if nums[j+1] < nums[j]: # 前一个数，就是i位置，但是需要该数需要一直往后，所以写成j+1方便j--
                    nums[j+1], nums[j] = nums[j], nums[j+1]
        print(nums)

# i = InsertSort()
# i.insert_sort([2, 3, 1, 4, 5])

class BinarySearchUnRecu:
    def binary_search(self, nums: List[int], target: int) -> Union[int, None]:
        if nums is None:
            return None
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

class BinarySearchRecu:
    def binary_search(self, nums:List[int], left: int, right: int, target: int) -> int:
        if nums is None:
            return -1
        if left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return self.binary_search(nums, mid+1, right, target)
            else:
                return self.binary_search(nums, left, mid-1, target)
        return -1


class FindLeftNum:
    def find_left_num(self, nums: List[int], target: int) -> int:
        idx = -1
        if nums is None:
            return idx
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] < target:
                left = mid + 1
            else:
                idx = mid
                right = mid - 1

        return idx

# f = FindLeftNum()
# print(f.find_left_num([1, 2, 2, 2, 3, 4, 5], 0))
#
# a = [2, 1, 4, 3, 5, 6, 7]


class LocalMinima:
    def print_local_minima_idx(self, nums: List[int]) -> int:
        # 左右边界条件
        if nums[0] < nums[1]:
            return 0
        n = len(nums)
        if nums[n-1] < nums[n-2]:
            return n-1
        idx = -1
        # 中间情况，由于0 -> 1 一定是升序，n-1 -> n-2 一定是降序，所以一定存在局部最小值。
        # 使用二分法，还是找两边升降序不一样的序列，一定存在局部最小值。
        left, right = 0, n-1
        # 画一下左右的趋势即可理解
        while left <= right:
            mid = ((right - left) >> 2) + left  # 一定要加括号！！
            idx = mid
            if nums[mid] > nums[mid-1]:
                right = mid -1
            elif nums[mid] < nums[mid+1]:
                return idx
            else:
                left = mid + 1
        return idx

l = LocalMinima()
print(l.print_local_minima_idx([6, 5, 4, 7, 5, 6, 7])) # 2
# print(l.print_local_minima_idx([6, 5, 4, 7, 5, 6, 7]))
#
# x = 6 >> 1
# print(x)

# b = BinarySearchRecu()
# print(b.binary_search([1, 2, 2, 2, 3, 4, 5],0, 6, 4))

class MergeSort:
    def merge_sort(self, nums: List[int]):
        if nums is None or len(nums) < 2:
            return

        return self.process(0, len(nums) - 1, nums) # 排序的过程
    def process(self, left: int, right: int, nums: List[int]):
        if left == right:
            return
        mid = ((right - left) >> 1) + left
        self.process(left, mid, nums) # 先归并排序好左边
        self.process(mid+1,right, nums) # 再归并排序好右边
        self.merge(left, mid, right, nums) # 最后将左右两边merge
    def merge(self, left: int, mid: int, right: int, nums: List[int]):
        result = [] # 先用一个辅助数组
        i, j = left, mid + 1 # 从左右两边开始归并
        while i <= mid and j <= right:
            if nums[i] < nums[j]:
                result.append(nums[i])
                i += 1
            else:
                result.append(nums[j])
                j += 1

        while i <= mid:
            result.append(nums[i])
            i += 1
        while j <= right:
            result.append(nums[j])
            j += 1

        for i in range(len(result)):
            # 一定要注意是left+i!!!因为要写回原数组！！！
            nums[left + i] = result[i]

def func(val1):
    val1[0] = 1

a = [2, 2, 2]
b = a



func(a)
print(a)
print(b)