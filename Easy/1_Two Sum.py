class Solution:
    def twoSum(self, nums, target: int):
        check = {}
        index = 0

        for index, num in enumerate(nums):
            if target-num in check:
                return [check[target-num],index]
            check[num] = index

sum = [2,7,11,15]
target = 9
print(Solution().twoSum(sum,target))

# O(n) time complexity and O(n) space complexity