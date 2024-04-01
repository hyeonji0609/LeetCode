# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def _dfs(root, path):
            nonlocal sum_count # sum_count는 _dfs의 local 변수가 아니다 == pathSum의 변수이다

            if not root:
                return
            # 지나가는 path에 무조건 노드 값을 더해주기
            path += root.val

            # target을 만났다면
            if path == targetSum:
                sum_count +=1 # count +1

            _dfs(root.left, path)
            _dfs(root.right, path)

        # 노드 자체를 순회하는 함수
        def node_search(root):
            if not root:
                return
            # _dfs에 0을 넣는 이유는 항상 path의 초기 값은 0이기 때문
            _dfs(root,0)

            
            node_search(root.left)
            node_search(root.right)
        
        sum_count=0
        node_search(root)

        return sum_count
