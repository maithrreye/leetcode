# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Recursive inorder solution 
TC O(N)
SC O(1)
Recursive stack O(H)

Make sure to have prev variable as Global. If its local then the recursion will give wrong result in some cases 

"""
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev= None # Set a global variable 
        return self.inorder(root)
    
    def inorder(self,root):
        #if self.prev and root:
            #print(self.prev.val,root.val)
            
        if root is None:
            return True 
        
        if self.inorder(root.left)==False:
            return False
        
        if (self.prev and self.prev.val>=root.val):
            return False
        
        self.prev=root
        return self.inorder(root.right)
