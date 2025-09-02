class Solution:
    def isValid(self, s: str) -> bool:
        
        paranthesis_holder = []

        for i in s:
            if i in "[{(":
                paranthesis_holder.append(i)
            if i in "}])":
                if len(paranthesis_holder) == 0:
                    return False
                removed_value = paranthesis_holder.pop()

                if removed_value == "[" and i != "]":
                    return False
                elif removed_value =="{" and i != "}":
                    return False
                elif removed_value =="(" and i !=")":
                    return False
        if len(paranthesis_holder) == 0:
            return True
        return False
    
s = Solution()

print(s.isValid("(]"))


#################### compact

class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]
        for i in s:
            if stk and ((stk[-1]=="(" and i==")") or  (stk[-1]=="[" and i=="]") or  (stk[-1]=="{" and i=="}")):
                stk.pop()
            else:
                stk.append(i)
        return len(stk)==0


# time complexity of the both problem is O(n) and space complexity is also O(n). if the order did not matter then the space complexity can reduced to the O(1)