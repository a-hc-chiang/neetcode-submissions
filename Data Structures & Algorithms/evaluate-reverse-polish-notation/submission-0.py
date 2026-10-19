from decimal import Decimal
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        res = 0 
        stk = []

        for token in tokens:
            # print(token, stk, token.isnumeric())
            if token != "+" and token != "-" and token != "*" and token != "/":
                stk.append(int(token))
            else:
                operand_a = stk[-1]
                stk.pop()
                operand_b = stk[-1]
                stk.pop()
                if token == "+":
                    stk.append(int(operand_b + operand_a))
                elif token == "-":
                    stk.append(int(operand_b - operand_a))
                elif token == "*":
                    stk.append(int(operand_b * operand_a))
                elif token == "/":
                    stk.append(int(operand_b / operand_a))
        # print(stk[-1])
        # if int(stk[-1]) + 0.5 <= stk[-1]:
        #     return int(stk[-1]) + 1
        return int(stk[-1])