from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        max_num = max(nums)
        max_num_index = nums.index(max_num)
        
        root = TreeNode(max_num)
        
        root.left = self.constructMaximumBinaryTree(nums[:max_num_index])
        
        root.right = self.constructMaximumBinaryTree(nums[max_num_index+1:])
        
        return root