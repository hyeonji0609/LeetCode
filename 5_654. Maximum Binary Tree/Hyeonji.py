# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def make_tree(nums):
            if len(nums) == 0 : # 리스트가 0이면 그냥 return
                return 
            else :
                base = TreeNode(max(nums)) # 제일 큰 값을 TreeNode class의 val 저장, base 변수에 할당
                idx = nums.index(max(nums)) # 제일 큰 값의 인덱스를 idx 변수로 저장
                
                left = nums[:idx] # 제일 큰 값 기준으로 리스트를 왼쪽으로 스플릿
                right = nums[idx+1:] # 오른쪽으로 스필릿
            
                base.left = make_tree(left) # 제일 큰 값의 왼쪽 값을 left에 저장
                base.right = make_tree(right) # 제일 큰 값의 오른쪽 값을 left에 저장
            
            return base
            
        return make_tree(nums)