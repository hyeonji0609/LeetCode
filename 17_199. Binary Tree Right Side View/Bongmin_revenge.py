# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        def dfs(node, depth):
            if node:
                # 깊이가 지금까지 들어온 ans랑 같으면 그 노드를 추가
                if depth == len(ans): # 처음 ans의 길이는 0 
                    ans.append(node.val)
                # right를 먼저 돌게 됨으로써 index와 depth를 맞춰줄 수 있다.
                dfs(node.right, depth+1)
                dfs(node.left, depth+1)
        ans = []
        dfs(root, 0)
        return ans