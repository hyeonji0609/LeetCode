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
                # 깊이는 결국 마지막 리프노드가 될 것 이기 때문
                dfs(node.right, depth+1)
                dfs(node.left, depth+1)
        ans = []
        dfs(root, 0)
        return ans