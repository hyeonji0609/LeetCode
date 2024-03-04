class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # leaf_node1과 2를 담을 리스트 초기화
        leaf_node1, leaf_node2 = [], []
        # 각 트리를 순회할 stack을 각 root노드부터 할당
        stack1, stack2 = [root1], [root2]
        # 첫번째 트리 순회
        while stack1:
            # stack1의 마지막 값을 pop하여 node로 할당
            node = stack1.pop()
            # node가 양쪽 자식 모두 없으면 그 node.val을 leaf_node1에 할당
            if node.left is None and node.right is None:
                leaf_node1.append(node.val)
            # node의 왼쪽 자식이 있으면 stack1에 할당
            if node.left:
                stack1.append(node.left)
            # node의 오른쪽 자식이 있으면 stack1에 할당
            if node.right:
                stack1.append(node.right)
        # 두번째 트리 순회
        while stack2:
            # stack2의 마지막 값을 pop하여 node로 할당
            node = stack2.pop()
            # node가 양쪽 자식 모두 없으면 그 node.val을 leaf_node2에 할당
            if node.left is None and node.right is None:
                leaf_node2.append(node.val)
            # node의 왼쪽 자식이 있으면 stack2에 할당
            if node.left:
                stack2.append(node.left)
            # node의 오른쪽 자식이 있으면 stack2에 할당
            if node.right:
                stack2.append(node.right)
        # 각 트리를 모두 순회한 후 leaf_node1과 2를 비교하여 return
        return leaf_node1 == leaf_node2
    
    '''
    Runtime 34 ms - Beats 76.26%
    Memory 16.58 MB - Beats 90.50%
    '''