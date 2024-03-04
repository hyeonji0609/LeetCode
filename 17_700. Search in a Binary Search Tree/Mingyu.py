class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # root를 node로 초기화
        node = root
        # node가 존재하는 동안 루프
        while node:
            # node.val이 val이면 node를 반환
            if node.val == val:
                return node
            # 그렇지 않고, node.val이 val보다 크면, node를 node.left로 할당
            elif node.val > val:
                node = node.left
            # node.val이 val보다 작으면, node를 node.right로 할당
            else:
                node = node.right
        # 루프가 종료되었음에도 node에 val이 없으면 None 반환
        return None
    
    '''
    Runtime 47 ms - Beats 94.02%
    Memory 18.34 MB - Beats 49.40%
    '''