class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def _preorder(node, count, now):
            # global은 함수 안에 정의된 것을 전역적으로 쓰고싶을 때
            # nonlocal은 함수 바깥에 정의된 것을 안에서 쓰고싶을 때 사용하면 된다

            nonlocal max_count


            if not node:
                return

            # max_count랑 지금까지 센거랑 비교해서 큰 값으로 업데이트 하겠다
            max_count = max(max_count, count)

            # node.left가 있을 때
            if node.left:
                # now가 "R"이라면 
                if now == "R":
                    # 재귀할 때 count에 +1 한 값으로 한번 더 재귀를 시키고 
                    # 왼쪽으로 갔으므로 now를 "L"로 업데이트
                    _preorder(node.left, count + 1, "L")
                else:
                    # 이 else문은 왼쪽으로 갈건데 왼쪽에서 왔다는 뜻이므로 다시 count를 1로 초기화
                    _preorder(node.left, 1, "L")
                    
            # node.right가 있을 때
            if node.right:
                # now가 "L"이라면
                if now == "L":
                    # left와 마찬가지로 count +1해주고
                    _preorder(node.right, count + 1, "R")
                else:
                    # 아니라면 다시 1로 초기화
                    _preorder(node.right, 1, "R")
                    
        max_count = 0
        _preorder(root, 0, None)
        return max_count

'''
runtime : 159ms 96.81%
memory : 30.44 62.44%
'''