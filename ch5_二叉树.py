import typing
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 二叉树的先序遍历--------------------------------------------------------------------------------------
class PreOrder:
    #  递归遍历需要把result也放在参数里面！！！
    def recur_pre_order(self, root: Optional[TreeNode], result: List[int]):
        if root is None:
            return 
        result.append(root.val)
        self.recur_pre_order(root.left, result)
        self.recur_pre_order(root.right, result)

    def unrecur_pre_order(self, root: Optional[TreeNode], result: List[int]):
        if root is None:
            return
        stack = [root]
        while len(stack) != 0:
            node = stack.pop()
            result.append(node.val)
            # 用栈的话，先右后左
            # 注意判断是否有左右孩子！
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)

# 二叉树的后序遍历--------------------------------------------------------------------------------------
class PostOrder:
    #  先左后右最后中
    def recur_post_order(self, root: Optional[TreeNode], result: List[int]):
        if root is None:
            return
        self.recur_post_order(root.left, result)
        self.recur_post_order(root.right, result)
        result.append(root.val)
    
    # 后序稍微复杂一些，需要把从stack出栈的元素，先放到栈里，最后按照出栈顺序输出，才是后序。
    def unrecur_post_order(self, root: Optional[TreeNode], result: List[int]):
        if root is None:
            return
        stack = [root]
        while len(stack) != 0:
            node = stack.pop()
            # 少用一个栈了，在0位置插入元素,模拟栈
            result.insert(0, node.val)
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
            
# 二叉树的中序遍历--------------------------------------------------------------------------------------
class InOrder:
    #  先左后右最后中
    def recur_in_order(self, root: Optional[TreeNode], result: List[int]):
        if root is None:
            return
        self.recur_in_order(root.left, result)
        result.append(root.val)
        self.recur_in_order(root.right, result)

    # 非递归中序遍历对于每个子树，整棵树左边界进栈。依次弹出节点的过程中，对弹出节点的右树重复。
    def unrecur_in_order(self, root: Optional[TreeNode], result: List[int]):
        if root is None:
            return
        stack = []
        node = root
        # 把所有的左边界压入
        while node is not None:
            stack.append(node)
            node = node.left
        while len(stack) != 0:
            # 先弹栈
            node = stack.pop()
            result.append(node.val)
            # 对右树周而复始
            cur = node.right
            while cur is not None:
                stack.append(cur)
                cur = cur.left

    # 左神的代码
    def z_unrecur_in_order(self, root: Optional[TreeNode], result: List[int]):
        if root is None:
            return
        stack = []
        # 把所有的左边界压入
        while len(stack) != 0 or root is not None:
            if root is not None:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                result.append(root.val)
                root = root.right



if __name__ == "__main__":
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    f = TreeNode(6)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    print(a.val)

    # # 先序遍历测试--------------------------------------------------------------------------------------
    # pre_order = PreOrder()

    # result = []
    # pre_order.recur_pre_order(a, result)
    # print(result)
    
    # result = []
    # pre_order.unrecur_pre_order(a, result)
    # print(result)

    # # 后序遍历测试--------------------------------------------------------------------------------------   
    # post_order = PostOrder()
    # result = []
    # post_order.recur_post_order(a, result)
    # print(result)

    # result = []
    # post_order.unrecur_post_order(a, result)
    # print(result)

    # # 中序遍历测试-------------------------------------------   
    # in_order = InOrder()
    # result = []
    # in_order.recur_in_order(a, result)
    # print(result)

    # result = []
    # in_order.unrecur_in_order(a, result)
    # print(result)

    # result = []
    # in_order.z_unrecur_in_order(a, result)
    # print(result)





