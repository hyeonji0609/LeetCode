# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        
        def _preorder(node, max_val, count):
            # 노드가 없으면 count를 반환
            if not node:
                return count
            # 노드가 있다면 이전의 맥스 값보다 현재 값이 더 좋으면 good 노드
            if node.val >= max_val:
                count +=1 

            # 최대값 업데이트
            max_val = max(max_val, node.val)

            # count는 재귀적으로 돌면서 계속계속 더해진 값으로 업데이트 if문에서 +1된 값이 리턴되기 때문
            count = _preorder(node.left, max_val, count)
            count = _preorder(node.right, max_val, count)

            return count

        # 초기 값으로 -inf를 주고 시작
        return _preorder(root, float('-inf'), 0)
    
'''
runtime : 152ms / beats : 15.28%
memory : 31.43mb / beats : 36.11%
'''