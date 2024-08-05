class Solution:
    def rotate(self, nums, k):
        k = k % len(nums)  # In case k is larger than the length of the list
        nums[:] = nums[-k:] + nums[:-k]  # Modify the list in-place


# Example usage:
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
solution = Solution()
solution.rotate(nums, k)
print(nums)  # Output should be [5, 6, 7, 1, 2, 3, 4]
