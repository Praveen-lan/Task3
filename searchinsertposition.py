class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

       
            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1

            # Search in left half
            else:
                right = mid - 1

        return left



obj = Solution()

print(obj.searchInsert([1,3,5,6], 5))  
print(obj.searchInsert([1,3,5,6], 2))  
print(obj.searchInsert([1,3,5,6], 7))  