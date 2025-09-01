import math
class Solution:
    def productExceptSelf(self, nums):
        output = [1]*len(nums)
        prefix = 1

        for i in range(len(nums)):
            output= prefix
            prefix*=nums[i-1]

        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            output[i]*=postfix
            postfix*=nums[i]
        
        return output

s = Solution()
print(s.productExceptSelf([-1,1,0,-3,3]))

# time complexity O(n) and space complexity O(n) for the array