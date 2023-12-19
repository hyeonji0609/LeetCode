class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root = TreeNode(preorder[0]) # 뿌리
        result = [root] # 처음 뿌리는 넣어주기
        
        for list_value in preorder[1:]: # 뿌리 다음 것부터 들고와서
            current_node = TreeNode(list_value)  # 현재 노드에 뿌리로 생성.
            prepare_var = result[-1] # 현재 비교할 변수 설정 result의 마지막 (처음은 8)
            
            if list_value < prepare_var.val:
                prepare_var.left = current_node
                result.append(list_value)
                
                
            elif list_value > prepare_var.val:
                
                for j in result[::-1]: # 저장된거에서 거꾸로 불러와서
                    if list_value > j.val: # 현재 preorder의 값과, 거꾸로 불러온 값을 차례대로 비교
                        # 현재 값이 크다면 result에 저장된 것에서 pop해서 비교 값으로 다시 넣어주기
                        prepare_var = result.pop() 
                    
                    else: # else는 result에서 preorder에 있는 거보다 크다는 거니까
                        break # break
                # 현재 값의 오른쪽으로 넣어주기 (크다는거니까)
                prepare_var.right = current_node 
                result.apend(current_node)
                        
        return root
                
# 못풀었습니다..