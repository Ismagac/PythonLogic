import re

class Solution:
    def isNumber(self, s: str) -> bool:
        pattern = r'^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$'
        return bool(re.match(pattern, s))

solution = Solution()
print(solution.isNumber("0"))       # True
print(solution.isNumber("e"))       # False
print(solution.isNumber("."))       # False
print(solution.isNumber("2e10"))    # True
print(solution.isNumber("-90E3"))   # True
print(solution.isNumber("53.5e93")) # True
print(solution.isNumber("1a"))      # False
print(solution.isNumber("e3"))      # False
print(solution.isNumber("99e2.5"))  # False
print(solution.isNumber("--6"))     # False
print(solution.isNumber("-+3"))     # False
print(solution.isNumber("95a54e53"))# False
