class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        output = []
        path = ""

        def preorder(root, output, path):
            if root: # root가 존재한다면
                path += str(root.val) # path 추가
                if root.left or root.right: # left나 right가 존재하면
                    path += "->" # 화살표 추가
                    # 현재 path : "root ->"
                    if root.left:
                        preorder(root.left, output, path)
                    if root.right:
                        preorder(root.right, output, path)
                else:
                    output.append(path)
            else:
                return

        preorder(root, output, path)
        
        return output

"""
Runtime: 40 ms
Memory Usage: 16.5 MB
"""