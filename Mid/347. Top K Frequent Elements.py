from collections import Counter

class Solution:
    def topKFrequent(self, nums, k: int):
        freq=Counter(nums)
        c=freq.most_common(k)
        print(classmethod)
        return [i for i,count in c]

s = Solution()
print(s.topKFrequent([1,1,1,2,2,3], 2))



## Time complexity O(n+mlogk), n is for Counter, as it builds a hash map of count and mlogk is to find most common class method. it uses heapq. Space complexity is for O(m), only to store frequencies.