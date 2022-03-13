# Time Complexity - O(n)
# Space Complexity - O(n)
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return None
        q = deque()
        q.append(root)
        result = []
        while len(q)!=0:
            size = len(q)
            temp = []
            for i in range(size):
                curr = q.popleft()
                temp.append(curr.val)
                if curr.left!=None:
                    q.append(curr.left)
                if curr.right!=None:
                    q.append(curr.right)
            result.append(temp)
        return result
