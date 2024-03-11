class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # 전위 순회
        def _preorder(node, depth, sum_dict):
            # 노드가 없으면 return 없음
            if not node:
                return 
            # 깊이가 딕셔너리 키들에 없다면 만들어주고 값을 현재 노드로 할당
            if depth not in sum_dict.keys():
                sum_dict[depth] = node.val
            # 깊이가 딕셔너리 키에 이미 있다면 현재 값을 계속 더해주기
            else:
                sum_dict[depth] += node.val
            left = _preorder(node.left, depth +1, sum_dict)
            right = _preorder(node.right, depth + 1,sum_dict)
        
        sum_dict={} # 딕셔너리 초기화
        _preorder(root, 0, sum_dict)

        # value들만 담아서 ls로 만들어주고
        ls = list(sum_dict.values())

        # 인덱스는 0부터 시작하므로 max값의 인덱스를 찾아서 +1 해주기
        return ls.index(max(ls))+1


'''
runtime : 184ms beats : 10.47% 런타임 매우 느림
memory : 19.96 beats : 70.81%
'''