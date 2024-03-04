class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # root가 None이면 0 return
        if root is None:
            return 0
        # depth를 0으로 초기화
        depth = 0
        # root노드를 stack에 할당
        stack = [root]
        
        # stack이 존재할 때까지 루프
        while stack:
            level_node_count = len(stack) # 현재 레벨의 노드 수
            for _ in range(level_node_count):
                node = stack.pop(0) # 현재 레벨의 노드를 하나씩 꺼냄
                # 자식 노드가 있으면 stack에 추가
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            depth += 1 # 현재 레벨의 모든 노드를 처리한 후 깊이 1 증가
        # 모두 순회 후 depth return
        return depth
    
    '''
    Runtime 41 ms - Beats 51.97%
    Memory 17.44 MB - Beats 98.54%
    '''