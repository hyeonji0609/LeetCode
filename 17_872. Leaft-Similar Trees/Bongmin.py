class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def find_leaves(node,ls):
            # 노드가 있지만
            if node:
                # 현재 노드에서 좌 우가 없다면 더이상 잎이 없으므로
                if not node.left and not node.right:
                    # 추가해주기
                    ls.append(node.val)
                # 전위순회     
                find_leaves(node.left, ls)
                find_leaves(node.right, ls)
        # 잎사귀들 초기화
        leaves_1 = []
        leaves_2 = []
        # roo1과 root2 각각 돌기
        find_leaves(root1,leaves_1)
        find_leaves(root2,leaves_2)

        if leaves_1 == leaves_2:
            return True
        
'''
runtime : 27ms beats : 97.2%
memory : 16.46 beats : 98.96
'''