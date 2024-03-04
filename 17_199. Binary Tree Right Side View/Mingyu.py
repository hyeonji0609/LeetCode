class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        right_most_node_at_depth = []
        stack = [(root, 0)] # stack에 루트 노드와 그 깊이를 0 짝지어 할당
        # stack이 None이 아닐 때까지 루프
        while stack:
            node, depth = stack.pop(0) # stack의 첫번째 쌍을 각각 node와 depth로 할당
            # (해당 깊이를 처음 방문했을 경우)
            if depth == len(right_most_node_at_depth): # pop된 depth와 right_most_node_at_depth의 길이가 같으면
                right_most_node_at_depth.append(node.val) # right_most_node_at_depth에 해당 node 추가
            # 해당 깊이 첫 방문이 아닐 시, 해당 깊이 인덱스의 값을 현재 node로 업데이트
            else:
                right_most_node_at_depth[depth] = node.val
            # node의 왼쪽자식이 있으면 stack에 왼쪽 자식과 그 깊이를 추가
            if node.left:
                stack.append((node.left, depth+1))
            # node의 오른쪽자식이 있으면 stack에 오른쪽 자식과 그 깊이를 추가
            if node.right:
                stack.append((node.right, depth+1))
        
        # 루프 종료 후 최종적으로 가장 우측 node만 담겨있음
        return right_most_node_at_depth
    
    '''
    Runtime 41 ms - Beats 24.32%
    Memory 16.51 MB - Beats 60.15%
    '''