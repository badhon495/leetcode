class Solution:
    def containsDuplicate(self, nums) -> bool:
        return len(set(nums)) != len(nums)
    

nums = [1,2,3,1]
sol = Solution()
print(sol.containsDuplicate(nums))

# O(n) time complexity and O(n) space complexity