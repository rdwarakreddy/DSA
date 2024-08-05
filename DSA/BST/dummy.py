# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def arrayToTree(self, root_array):
        """
        Converts array representation to binary tree.
        :type root_array: List[int]
        :rtype: TreeNode
        """
        if not root_array:
            return None

        # Create nodes and store them in a list
        nodes = [None] * len(root_array)
        for i in range(len(root_array)):
            if root_array[i] is not None:
                nodes[i] = TreeNode(root_array[i])

        # Fill the left and right children
        for i in range(len(root_array)):
            if nodes[i] is not None:
                left_index = 2 * i + 1
                right_index = 2 * i + 2
                if left_index < len(nodes) and nodes[left_index] is not None:
                    nodes[i].left = nodes[left_index]
                if right_index < len(nodes) and nodes[right_index] is not None:
                    nodes[i].right = nodes[right_index]

        return nodes[0]  # Return the root of the tree


# Example usage
root_array = [3, 9, 20, None, None, 15, 7]  # Example binary tree in array form
solution = Solution()
print(solution.arrayToTree(root_array))
