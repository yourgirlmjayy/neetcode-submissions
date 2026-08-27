class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {')':'(', '}':'{', ']':'['}

        for bracket in s:
            # if its a closing bracket, pop from the stack
            if bracket in brackets and len(stack) > 0: 
                open_bracket = stack.pop()
                # return false if the brackets do not match
                if brackets[bracket] != open_bracket:
                    return False
            else:
                stack.append(bracket)
        return len(stack) < 1



        