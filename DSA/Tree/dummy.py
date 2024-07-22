# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: List[int]
        :rtype: int
        """
        if not root:
            return 0

        last_index = len(root) - 1
        depth = 0

        while last_index > 0:
            last_index = (last_index - 1) // 2
            depth += 1

        return depth + 1  # +1 to count the root level


root = [3, 9, 20, None, None, 15, 7]  # Example binary tree in array form
solution = Solution()
print(solution.maxDepth(root))  # Output: 3
