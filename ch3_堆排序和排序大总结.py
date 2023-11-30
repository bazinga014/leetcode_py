from typing import List
import heapq
class BigHeap:
    # 某个数现在处在index位置，能否往上移动
    def heap_insert(self, nums: List[int], index: int):
        while index > 0 and nums[index] > nums[(index - 1) // 2]:
            nums[index], nums[(index - 1) // 2] = nums[(index - 1) // 2], nums[index]
            index = (index - 1) // 2

    # 某个数现在在index位置，能否往下移动
    def heapify(self, nums: List[int], index: int, heap_size: int):
        left = index * 2 + 1 # 左孩子下标
        while left < heap_size: # 下方还有孩子的时候
            # 孩子中最大值的下标给largest
            largest = left+1 if left+1 < heap_size and nums[left+1] > nums[left] else left
            # 孩子中最大的和当前位置的值比
            largest = largest if nums[largest] > nums[index] else index
            # 不比父亲的值大，结束
            if largest == index:
                break
            # 否则孩子和父亲的值交换，继续往下和孩子比
            nums[largest], nums[index] = nums[index], nums[largest]
            index = largest
            left = index * 2 + 1

    def heap_sort(self, nums: List[int]): # 总体复杂度O(NlogN)
        if len(nums) < 2:
            return
        # 建堆  整体复杂度是O(NlogN)
        # for i in range(0, len(nums)): # O(N)
        #     self.heap_insert(nums, i) # O(logN)

        # 建堆2 整体复杂度是O(N)。因为往下heapify，完全二叉树的最底下一层（大概是N/2个结点）都不需要动
        # T(N) = (N/2)*1 (看了一眼) + 2*(N/4) + ... 经计算则是O(N)
        for i in range(len(nums), -1, -1):
            self.heapify(nums, i, len(nums))

        # 维护堆
        heap_size = len(nums)
        # 每次都把头结点的值换到最后，然后0位置的值做heapify，完成后heapsize-=1
        nums[0], nums[heap_size-1] = nums[heap_size-1], nums[0]
        heap_size -= 1
        while heap_size > 0: # O(N)
            self.heapify(nums,0, heap_size) # O(logN)
            nums[0], nums[heap_size - 1] = nums[heap_size - 1], nums[0]
            heap_size -= 1

# arr = [1,3,2,4,5,3,4,6,2,7]
# h = BigHeap()
# h.heap_sort(arr)
# print(arr)

class SortedArrDistanceLessK:
    def sorted_less_k(self, nums: List[int], k: int):
        if len(nums) < 2:
            return
        n = len(nums)
        # 建堆
        heap_size = min(n, k+1) # 基本上就等于k+1
        heapq.heapify(nums[0:heap_size]) # 建立[0, k]
        i = 0
        heap_idx = heap_size
        while heap_idx < n:
            nums[i] = heapq.heappop(nums[i:heap_idx])  # [0, k]的堆取出堆首元素放在nums[i]上。
            i += 1
            heap_idx += 1
            heapq.heapify(nums[i:heap_idx]) # 往后移一个位置，加入堆
        # 出循环后，堆上应该还有k+1个元素，一个一个弹出即可。
        while i < n:
            nums[i] = heapq.heappop(nums[i:n])
            i += 1







