class Solution(object):
    def removeElement(self, nums, val):
        k = 0   # Pointer for placing non-val elements

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k


# Example Usage
obj = Solution()

nums1 = [3, 2, 2, 3]
k1 = obj.removeElement(nums1, 3)
print(k1)          # 2
print(nums1[:k1])  # [2, 2]

nums2 = [0,1,2,2,3,0,4,2]
k2 = obj.removeElement(nums2, 2)
print(k2)          # 5
print(nums2[:k2])  # [0,1,3,0,4]