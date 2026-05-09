class Solution():
    def isPalindrome(self, x):
        if x < 0:
            return False
        s = str(x)
        return s == s[::-1]
obj = Solution()
print(obj.isPalindrome(121))
print(obj.isPalindrome(-121))
print(obj.isPalindrome(10))