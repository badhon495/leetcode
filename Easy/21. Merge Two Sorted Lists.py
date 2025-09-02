class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:   
        if not l1 or not l2:
            return l1 or l2
        
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

# time complexity O(n+m), sum of length n and m. the space complexity would be O(1) as we are not using recurssion stack