class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # 전위 순회
        def bst(root, val):
            # root가 없거나 현재 노드가 == val 이라면
            if not root or root.val == val:
                return root # 그대로 root를 반환 
            # val이 root.val보다 작으면 왼쪽으로 가고
            if val < root.val:
                bst(root.left, val)
            # 아니라면 오른쪽으로 가기.
            else:
                bst(root.right, val)
        # 시작
        bst(root,val)
'''
이러면 비어있을 때도 되지 않을까 해서했는데 안됨 
            2
           / \
          1   3
1 번째 조건에서 root.val == val에 걸려서 그대로 root가 나오면 되는데 왜 안되지..
왜 output이 []인지 모르겠다..
'''
            
            
'''
fail 인 줄 알았으나
return bst(root,val)로 해결
'''

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def bst(root,val):
            if not root or root.val == val:
                return root
            
            if val < root.val:
                return bst(root.left, val)
            else:
                return bst(root.right, val)
        return bst(root,val)