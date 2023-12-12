# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        # output 트리의 초기(임시) 루트
        output_root = TreeNode(0)
        self.current = output_root

        # 중위순회 함수 생성
        def inorder(node):
            # node가 비어있으면 inorder 함수 실행 종료
            if not node:
                return None
            
            # 왼쪽 자식을 방문
            inorder(node.left)

            # 현재 노드를 output 트리에 추가
            node.left = None # 왼쪽 자식을 None으로 설정
            self.current.right = node # 현재 노드를 이전 노드의 오른쪽 자식으로 설정
            self.current = node # 현재 노드를 업데이트

            # 오른쪽 자식을 방문
            inorder(node.right)

        # 중위 순회 시작
        inorder(root)

        # output 트리의 오른쪽 자식이 output 트리의 실제 루트
        return output_root.right
    
'''
Runtime 44 ms - Beats 20.98%
Memory 16.4 MB - Beats 54.8%
'''