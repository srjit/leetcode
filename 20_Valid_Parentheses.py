
class Solution:

    def isValid(self, s):

        complement = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        stack = []
        for ch in s:
            if ch not in complement:
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                else:
                    value_at_stack_top = stack.pop()
                    paranthesis_l = complement[ch]
                    if value_at_stack_top != paranthesis_l:
                        return False
        return True

s = Solution()
print(s.isValid("()[]{}}"))