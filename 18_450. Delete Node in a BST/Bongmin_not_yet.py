# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def get_leftmost(node):
            while node.left:
                node = node.left
            return node
        #재귀적으로 삭제 처리할 함수
        def _delete(node, data):
            if node is None:
                return

            #삭제할 노드가 현재 노드보다 작으면 왼쪽에서 찾아서 삭제
            #삭제할 노드가 현재 노드보다 크면 오른쪽에서 찾아서 삭제
            if node.val >  :
                node.left = _delete(node.left, data)
            elif node.val < data:
                node.right = _delete(node.right, data)
            else: 
                #삭제할 노드를 찾았고, 자식노드가 둘이면
                #삭제할 노드의 오른쪽에서 가장 작은(왼쪽) 노드를 찾는다.
                #삭제할 노드의 값을 가장 왼쪽 노드의 값으로 대체한다.
                #가장 왼쪽 노드를 삭제하고, 결과를 반환한다.
                if node.left and node.right:
                    leftmost = get_leftmost(node.right)
                    node.val = leftmost.data
                    node.right = _delete(node.right, leftmost.data)
                    return node

                #자식이 하나이거나 리프 노드이면 해당 자식을 반환
                if node.left:
                    return node.left
                else:
                    return node.right
            return node
        _delete(root,key)