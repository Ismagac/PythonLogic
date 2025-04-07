class Solution:
    def calculate(self, s: str) -> int:
        def helper(it):
            stack = []
            num = 0
            sign = 1

            while True:
                try:
                    c = next(it)
                except StopIteration:
                    break

                if c.isdigit():
                    num = num * 10 + int(c)
                elif c == '+':
                    stack.append(sign * num)
                    num = 0
                    sign = 1
                elif c == '-':
                    stack.append(sign * num)
                    num = 0
                    sign = -1
                elif c == '(':
                    num = helper(it)
                elif c == ')':
                    stack.append(sign * num)
                    return sum(stack)
                elif c == ' ':
                    continue

            stack.append(sign * num)
            return sum(stack)

        return helper(iter(s))


s = Solution()

print(s.calculate("1 + 1"))                 # 2
print(s.calculate(" 2-1 + 2 "))             # 3
print(s.calculate("(1+(4+5+2)-3)+(6+8)"))    # 23