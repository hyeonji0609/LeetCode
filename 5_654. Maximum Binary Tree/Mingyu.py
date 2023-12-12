# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # nums가 비어있으면 None을 반환
        if not nums:
            return None
        
        # 1번: nums에서 가장 큰 값과 그 인덱스 찾기
        max_val = max(nums)
        max_index = nums.index(max_val)
        
        # 2번: TreeNode의 root를 max_val로 지정
        root = TreeNode(max_val)

        # 3번: root의 left_prefix를 left로 할당
        root.left = self.constructMaximumBinaryTree(nums[:max_index])
        
        # 4번: root의 right_suffix를 right로 할당
        root.right = self.constructMaximumBinaryTree(nums[max_index+1:])

        # 재귀적으로 root 업데이트
        return root
    
    
'''
Runtime 166 ms - Beats 70.7%
Memory 16.9 MB - Beats 80.60%
'''