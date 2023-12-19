# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        temp = TreeNode(0) # 임시 노드 생성
        root = TreeNode(preorder[0]) # root 노트 생성
        stack = [root] # 스택 생성

        for i in preorder[1:]: # root 제외 preorder 리스트 반복
            node = TreeNode(i) # 노드 생성
            if node.val < stack[-1].val: # top의 값이 현재 노드의 값보다 작으면 왼쪽 노드로 + 스택
                stack[-1].left = node
                stack.append(node)
            else:
                while stack and (node.val > stack[-1].val): # 스택이 존재 + 현재 값보다 큰 값과 작은 값 사이를 갖도록 반복
                    temp = stack.pop()
                temp.right = node # 오른쪽 가지로 지정
                stack.append(node) # 스택

        return root 

"""
Runtime 42 ms
Memory 16.5 MB
"""