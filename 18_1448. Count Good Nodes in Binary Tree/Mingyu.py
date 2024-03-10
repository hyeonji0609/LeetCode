class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            # 현재 node가 없으면 더이상 자식이 없으므로 0을 반환
            if not node:
                return 0
            # good_node_count에 현재 node의 값이 max_val(경로상의 최댓값) 이상이면, 1을 그렇지 않으면 0을 할당
            good_node_count = 1 if node.val >= max_val else 0
            #  max_val(경로상의 최댓값)을 현재 노드의 값과 비교하여 더 큰 값으로 업데이트
            max_val = max(max_val, node.val)
            # 현재 노드의 왼쪽자식들에 dfs를 재귀적으로 적용하고, good_node_count의 갯수를 더해줌.
            good_node_count += dfs(node.left, max_val)
            # 현재 노드의 오른쪽자식들에 dfs를 재귀적으로 적용하고, good_node_count의 갯수를 더해줌.
            good_node_count += dfs(node.right, max_val)
            # 재귀적으로 업데이트 된 good_node_count를 반환
            return good_node_count
        # root와 max_val을 루트값으로하여 재귀적으로 dfs를 적용한 값을 리턴
        return dfs(root, root.val)
    
    '''
    Runtime 138 ms - Beats 42.66%
    Memory 31.46 MB - Beats 37.20%
    '''