class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0

        # 재귀적 Depth-First Search (prefix Sum 접근법)
        def dfs(node, curr_sum, targetSum):
            # node가 없으면 0을 리턴
            if not node:
                return 0

            res = 0 # res를 0으로 초기화
            curr_sum += node.val # node.val을 누적합 계산

            # 현재 노드까지의 누적합에서 targetSum을 뺀 값이 mapping에 존재하면
            # 현재 path의 한 node에서 targetSum만큼의 합을 가진 하위 경로가 존재함을 의미
            # 따라서 해당 경우 res에 해당 경로의 수 추가
            if (curr_sum - targetSum) in mapping:
                res += mapping[curr_sum - targetSum]
            # 현재 노드까지의 누적합이 mapping에 존재하면
            # mapping에 해당 경로의 수 누적해서 추가
            if curr_sum in mapping:
                mapping[curr_sum] += 1
            # 현재 노드까지의 누적합이 mapping에 존재하지 않으면
            # mapping에 해당 경로의 수 1 추가
            else:
                mapping[curr_sum] = 1
            
            # 현재 노드의 왼쪽 서브트리와 오른쪽 서브트리 각각 순회하여 res 업데이트
            res += dfs(node.left, curr_sum, targetSum)
            res += dfs(node.right, curr_sum, targetSum)
            # 재귀호출이 끝난 후 현재 노드를 제외하기 위해 - 1
            mapping[curr_sum] -= 1
            # res return
            return res

        # collections 모듈에 포함된 defaultdict 클래스의 인스턴스
        # 기본 dict와 유사하지만, dict에 key가 없는 경우 미리 정의된 int()를 호출해 key를 기본값 0으로 초기화
        # curr_sum을 key로 하고, 해당 curr_sum을 가진 path의 수를 value로 하는 dict
        mapping = defaultdict(int) 
        # curr_sum이 정확히 targetSum과 일치하는 경우를 위해 mapping[0] = 1로 초기화
        mapping[0] = 1

        return dfs(root, 0, targetSum)