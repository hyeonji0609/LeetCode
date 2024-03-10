# 풀이 1
import numpy as np
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return []
        # level별 합계 계산할 리스트 생성
        node_at_level_sum = []
        # 스택에 root와 그 레벨을 0으로 할당
        stack = [(root, 0)]
        # 스택이 존재할 때까지 루프
        while stack:
            # stack의 첫번째 값을 pop하여 node와 level로 할당
            node, level = stack.pop(0)
            # level별 합계 리스트의 길이와 level이 같으면(첫번째 방문)
            if level == len(node_at_level_sum):
                # 리스트에 node 할당
                node_at_level_sum.append(node.val) 
            # 그렇지 않으면, (두번째 방문)
            else:
                # 리스트에 level 인덱스에 값을 현재 노드의 값과 합산하여 업데이트
                node_at_level_sum[level] = node_at_level_sum[level] + node.val
            # 현재 노드의 왼쪽 자식이 있으면 스택에 왼쪽자식과 level+1을 할당
            if node.left:
                stack.append((node.left, level+1))
            # 현재 노드의 오른쪽 자식이 있으면 스택에 오른쪽자식과 level+1을 할당
            if node.right:
                stack.append((node.right, level+1))
        # 루프 종료 후에 node_at_level_sum의 최댓값의 인덱스를 반환하여 + 1하여 리턴
        # (root의 level을 0으로 가정했기 때문)
        return np.argmax(node_at_level_sum) + 1
    
    '''
    Runtime 257 ms - Beats 5.03%
    Memory 40.13 MB - Beats 8.28%
    '''

# 풀이 2
from collections import deque

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        # 최댓값에 초기값을 굉장히 작은 수로 할당
        max_sum = float('-inf')
        # 최대 레벨의 초기값을 0으로 할당
        max_level = 0
        # 현재 레벨을 1로 할당
        current_level = 1
        # 큐에 root와 그 level을 1로 튜플로 할당
        queue = deque([(root, 1)])
        # 큐가 존재할 때까지 루프
        while queue:
            # level_sum의 초기값을 0으로 할당
            level_sum = 0
            # level_length(해당 레벨의 노드 수)를 큐의 길이로 할당
            level_length = len(queue)
            # 현재 레벨의 노드 수만큼 for 루프
            for _ in range(level_length):
                # 큐의 가장 왼쪽 값을 node와 level로 반환
                node, level = queue.popleft()
                # level_sum에 node.val을 합산해서 업데이트
                level_sum += node.val
                # 왼쪽 자식이 있으면 큐에 왼쪽 자식과 level+1을 할당
                if node.left:
                    queue.append((node.left, level + 1))
                # 오른쪽 자식이 있으면 큐에 오른쪽 자식과 level+1을 할당
                if node.right:
                    queue.append((node.right, level + 1))
            # for 루프 종료 후 level_sum과 max_sum을 비교하여
            # level_sum이 더 크면,
            if level_sum > max_sum:
                # max_sum을 level_sum으로 업데이트하고
                # 그 level을 max_level로 업데이트
                max_sum = level_sum
                max_level = level
            # 현재 레벨을 1 증가
            current_level += 1
        # 루프 종료 후, max_sum이 있는 level을 리턴
        return max_level
    
    '''
    Runtime 159 ms - Beats 51.11%
    Memory 19.94 MB - Beats 71.44%
    '''