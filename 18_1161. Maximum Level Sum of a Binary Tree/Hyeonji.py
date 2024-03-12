class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        depthSum = dict()
        depth = 1
        depthSum[depth] = root.val
        
        def bfs(root, depth, depthSum):
            if root is None:
                return

            depth += 1
            right = root.right
            left = root.left

            if left and right:
                if depth in depthSum:
                    depthSum[depth] += left.val + right.val
                else:
                    depthSum[depth] = left.val + right.val
                bfs(right, depth, depthSum)
                bfs(left, depth, depthSum)
            elif (left is None) and right :
                if depth in depthSum:
                    depthSum[depth] += right.val
                else:
                    depthSum[depth] = right.val
                bfs(right, depth, depthSum)
            elif (right is None) and left :
                if depth in depthSum:
                    depthSum[depth] += left.val
                else:
                    depthSum[depth] = left.val
                bfs(left, depth, depthSum)
            else :
                return
        
        bfs(root, 1, depthSum)
        
        return max(depthSum, key=depthSum.get)

"""
Runtime: 162 ms
Memory Usage: 19.9 MB
"""