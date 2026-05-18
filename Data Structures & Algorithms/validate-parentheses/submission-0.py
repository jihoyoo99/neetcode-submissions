class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        store = {")":"(", "}":"{", "]":"["}
        for b in s:
            #if closing bracket
            if b in store:
                if stack and stack[-1] == store[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
        return stack == []