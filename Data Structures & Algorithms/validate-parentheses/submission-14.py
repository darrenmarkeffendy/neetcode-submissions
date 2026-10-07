class Solution:
    def isValid(self, s: str) -> bool:
        open_bracket = ['(','{','[']
        close_bracket = [')','}',']']
        stack = []
        
        if len(s) % 2 != 0:
            return False


        for character in s:
            if character in open_bracket:
                stack.append(character)
            elif character in close_bracket:
                if not stack:
                    return False
                else:
                    if character == ')' and stack.pop() == '(':
                        continue
                    elif character == '}' and stack.pop() == '{':
                        continue
                    elif character == ']' and stack.pop() == '[':
                        continue
                    else:
                        return False
            else:
                return False

                
        if not stack:
            return True
        else:
            return False


            
