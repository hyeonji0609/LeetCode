# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

            def dfs(node, depth):
                # 노드가 없으면 그냥 그 깊이 반환(초기값 0)
                if not node: 
                    return depth
                # 왼쪽부터 갈건데 처음에는 node == root이므로 root.left가 된다
                # 한칸 내려갔으므로 depth 1증가
                left = dfs(node.left, depth + 1)
                # 왼쪽 다 돌았으면 오른쪽으로 갈건데
                # 마찬가지로 돌 때마다 깊이 1씩 증가시켜주기
                right = dfs(node.right, depth + 1)
                # left와 right의 길이가 다른 경우가 있으므로 큰 것 반환
                return max(left, right)

            return dfs(root, 0)
'''
Runtime : 31ms beats : 96.59%
memory : 17.68 beats : 62.69

'''