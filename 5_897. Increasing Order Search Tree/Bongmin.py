# 못풀었습니다.. 하지만 찾아보던 중 중위순회의 개념을 알게되어
# Stack을 이용한 이진탐색트리에서 중위순회하는 방법을 공유합니다!!

def inorder(tree):
    
    index = 0  
    res, stack = [],[]
    
    while True:
        if index < len(tree) and tree[index] is not None:
            stack.append(index)
            index = 2 * index + 1
        elif stack:
            index = stack.pop()
            res.append(tree[index])
            index = 2 * index + 2
        else:
            break

    return res

root = [5,3,6,2,4,None,8,1,None,None,None,7,9]
inorder(root)

# 인덱스 변화 과정 
# 처음 인덱스는 0이다. 이때 root[0] == 5이다.
# while문 안에서 
# 0은 root의 길이보다 짧고, root[0] != none이므로 if문안에서 돈다
# stack에 0을 어펜드하고 index를 2 * 0 + 1 = 1, 1을 업데이트 한다.

# ==================================
# TreeNode inorder방식으로 푼 방법 # 공부하면서 풀었기 때문에 방식은 같습니다.
# ==================================

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        output_root = TreeNode(0)
        self.current = output_root
        
        def inorder(node):
            
            if not node:
                return None
                
            inorder(node.left)
            
            node.left = None
            self.current.right = node
            self.current = node
            
            inorder(node.right)
            
        inorder(root)
        
        return output_root.right

        
