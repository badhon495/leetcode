class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        first = 0
        last = len(s)-1

        while first <= last:
            if s[first].isalnum() is False:
                last-=1
            elif s[first] == s[last]:
                first+=1
                last-=1
                continue
            else:
                return False
        return True
    

s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))

# here the time complexity is O(n) and space complexity is also O(n) as i am creating a new list with lower. to minimize this you can ue the following method

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left,right=0,len(s)-1
        while left<right:
            while left<right and not s[left].isalnum():
                left +=1
            
            while left<right and not s[right].isalnum():
                right -=1
            
            if s[left].lower()!=s[right].lower():
                return False
            
            left +=1
            right -=1
        return True

# this method directly uses the lower method when it is needed and not creating a list.