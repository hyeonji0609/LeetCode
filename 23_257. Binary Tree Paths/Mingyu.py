class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = [] # 결과 리스트
        path = "" # path 문자열로 초기화

        def dfs(root, path):
            if not root: # root가 아니면 종료
                return
            # path에 root.val 문자열로 할당
            path += str(root.val)
            # root가 자식이 있으면,
            if root.left or root.right:
                # path에 화살표 추가
                path += "->"
                # 왼쪽 자식 재귀
                if root.left:
                    dfs(root.left, path)
                # 오른쪽 자식 재귀
                if root.right:
                    dfs(root.right, path)
            # 다 돌고 나면 result에 path 할당
            else:
                result.append(path)
                
        dfs(root, path)
        return result
    '''
    Runtime 28 ms - Beats 95.32%
    Memory 16.56 MB - Beats 46.88%
    '''