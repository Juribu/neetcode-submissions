class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for char in s:
            print(stack)
            if char == '[' or char == '(' or char == '{':
                stack.append(char)
            elif not stack:
                return False
            elif char == ']':
                if stack.pop() != '[':
                    return False
            elif char == '}':
                if stack.pop() != '{':
                    return False
            elif char == ')':
                if stack.pop() != '(':
                    return False
                
        return not stack


