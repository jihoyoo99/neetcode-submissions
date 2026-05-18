class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        store = {")":"(", "}":"{", "]":"["}
        #minor optimization, checks for early exit
        if len(s)%2 != 0:
            return False
        for b in s:
            #if closing bracket
            if b in store:
                if stack and stack[-1] == store[b]:
                    stack.pop()
                else:
                    return False
            #if opening bracket
            else:
                stack.append(b)
        return stack == []