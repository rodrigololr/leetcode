class Solution(object):
    def evalRPN(self, tokens):
        stack_numbers = []
        
        for token in tokens:
            if token == '+':
                num2 = stack_numbers.pop()
                num1 = stack_numbers.pop()
                stack_numbers.append(num1 + num2)
            elif token == '-':
                num2 = stack_numbers.pop()
                num1 = stack_numbers.pop()
                stack_numbers.append(num1 - num2)
            elif token == '*':
                num2 = stack_numbers.pop()
                num1 = stack_numbers.pop()
                stack_numbers.append(num1 * num2)
            elif token == '/':
                num2 = stack_numbers.pop()
                num1 = stack_numbers.pop()
                stack_numbers.append(int(num1/float(num2)))
            else:
                stack_numbers.append(int(token))
        return stack_numbers[-1]

        
