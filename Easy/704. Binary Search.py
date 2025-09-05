class Solution:
    def search(self, nums, target):

        left, right = 0, len(nums)-1

        while left <= right:
            middle = (left+right)//2

            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle-1
            elif nums[middle] < target:
                left = middle+1
        return -1
        
s = Solution()
print(s.search([5],5))
    

# time would be O(logn) and space would be O(1) as there is not muc variable we are creating.