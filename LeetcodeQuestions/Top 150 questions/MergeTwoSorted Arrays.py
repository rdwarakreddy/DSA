class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # Merge nums1 and nums2 into nums1
        nums1[m:] = nums2[:n]

        # Sort the combined array
        nums1.sort()


# Example usage
sol = Solution()
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
sol.merge(nums1, m, nums2, n)
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]
