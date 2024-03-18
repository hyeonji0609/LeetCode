class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        # 루트가 없으면 0을 반환
        if not root:
            return 0
        
        # 최대 지그재그 길이 0으로 초기화
        max_zigzag_length = 0
        # stack에 튜플로 (root, 이전 노드 방향, 현재 지그재그 길이) 할당
        stack = [(root, False, 0), (root, True, 0)]  # 각각 왼쪽자식, 오른쪽자식으로
        
        # 스택이 존재할 때까지 루프
        while stack:
            # 스택의 마지막 인자를 각 변수에 할당
            node, is_left, length = stack.pop()
            # 현재 지그재그 길이랑 최대 지그재그 길이를 비교하여 업데이트
            max_zigzag_length = max(max_zigzag_length, length)
            # 현재 방향이 왼쪽인 경우
            if is_left:
                # 오른쪽 자식이 있으면, 해당 노드를 스택에 추가하고, 현재 지그재그 길이 1 증가
                if node.right:
                    stack.append((node.right, False, length + 1))
                # 왼쪽 자식이 있으면, 해당 노드를 스택에 추가하고, 현재 지그재그 길이는 1
                # (왼-왼은 카운트 x)
                if node.left:
                    stack.append((node.left, True, 1))
            # 현재 방향이 오른쪽인 경우
            else:
                # 왼쪽 자식이 있으면, 해당 노드를 스택에 추가하고, 현재 지그재그 길이 1 증가
                if node.left:
                    stack.append((node.left, True, length + 1))
                # 오른쪽 자식이 있으면, 해당 노드를 스택에 추가하고, 현재 지그재그 길이는 1
                # (오-오는 카운트 x)
                if node.right:
                    stack.append((node.right, False, 1))
        # 루프 종료 후 최대 지그재그 길이 리턴
        return max_zigzag_length
    
    '''
    Runtime 198 ms - Beats 44.04%
    Memory 25.77 MB - Beats 97.72%
    '''