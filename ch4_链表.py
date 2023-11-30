from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

l1 = ListNode()
l2 = ListNode()
l3 = ListNode()
l4 = ListNode()

l1.val = 4
l2.val = 5
l3.val = 6
l4.val = 7
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = None

class Solution:
    def reserve_list(self, head: Optional[ListNode])-> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        # 创建一个临时头结点
        tmp_head = ListNode()
        tmp_head.next = None

        while head is not None:
            p_next = head.next # 创建一个p_next节点记录head的next，防止断链
            head.next = tmp_head.next
            tmp_head.next = head
            head = p_next

        return tmp_head.next

# head1 = l1
# while head1 is not None:
#     print(head1.val)
#     head1 = head1.next
#
# s = Solution()
# head2 = s.reserve_list(l1)
# while head2 is not None:
#     print(head2.val)
#     head2 = head2.next

class PalindromeList:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        stack = []
        p_next = head
        while p_next is not None:
            stack.append(p_next.val)
            p_next = p_next.next

        p_next = head
        for i in range(len(stack)):
            if p_next.val != stack[len(stack) -1 - i]:
                return False
            p_next = p_next.next

        return True

    # def print_reverse(head):
    #     if head is not None:
    #         print_reverse(head.next)

class ParitionListNode:
    def partion(self, head: ListNode, target: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        less_head = less_tail = equal_head = equal_tail = more_head = more_tail = None
        p_next = head
        while p_next is not None:
            if p_next.val < target:
                if less_head is None:
                    less_head = p_next
                # 【这个if-else】
                if less_tail is None:
                    less_tail = p_next
                else:
                    less_tail.next = p_next
                    less_tail = p_next

            elif p_next.val == target:
                if equal_head is None:
                    equal_head = p_next
                # 可以把上面的【这个if-else】简写成下面三句
                if equal_tail is not None:
                    equal_tail.next = p_next
                equal_tail = p_next

            else:
                if more_head is None:
                    more_head = p_next
                if more_tail is not None:
                    more_tail.next = p_next
                more_tail = p_next

            p_next = p_next.next
        #首尾相连时，一定要讨论清楚情况！没有小于等于大于区域时，会有空指针！！！
        if less_tail is not None:
            if equal_head is not None:
                less_tail.next = equal_head
                equal_tail.next = more_head
            else:
                less_tail.next = more_head
            return less_head
        else:
            if equal_head is not None:
                equal_tail.next = more_head
                return equal_head
            else:
                return more_head


p = ParitionListNode()
x = p.partion(l1, 3)
while x is not None:
    print(x.val)
    x = x.next

