# class Father:
#     def property(self):
#         print("the father have lot have money")
#
#
# class Son(Father):
#
#     def selfMoney(self):
#         print("the son also have money but less than from father money")
#
#
# obj = Son()
# obj.property()
# obj.selfMoney()


# import pandas as pd
#
# data = {"Name": ["Alice", "Bob", "charlis"], "Age": [25, 35, 65], "city": ["London", "USA", "paris"]}
# df = pd.DataFrame(data)
#


def evaluate_postfix(expression):
    stack = []

    for token in expression.split(','):
        if token.isdigit():
            stack.append(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if token == '+':
                stack.append(operand1 + operand2)
            elif token == '-':
                stack.append(operand1 - operand2)
            elif token == '*':
                stack.append(operand1 * operand2)
            elif token == '/':
                stack.append(operand1 / operand2)

    return stack.pop()


# Example usage:
postfix_expression = "6,4,3,-,*,5,7,2,-,/,+"
result = evaluate_postfix(postfix_expression)
print("Result:", result)
























