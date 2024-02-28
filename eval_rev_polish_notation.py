'''You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.'''

# Had to look in the solutions for this one. Figuring out how to solve it is the tricky part. Implementation is easy

import math

# Helper to evaluate based on operand. Make sure variables are in the correct order
def evaluate(var2, var1, operand):
    if operand == '-':
        return var1 - var2
    if operand == '+':
        return var1 + var2
    if operand == '/':
        return math.trunc(var1 / var2)
    if operand == '*':
        return var1 * var2
# Iterate tokens and append numbers to the stack
# When an operand is reached, pop most recent two vals and evaluate, push result onto the stack
def eval_RPN(tokens):
    stack = []
    for token in tokens:
        if token.isdigit() or len(token) > 1:
            stack.append(int(token))
        else:
            val1 = stack.pop()
            val2 = stack.pop()
            output = evaluate(val1, val2, token)
            stack.append(output)
    return stack.pop()

# TESTS

print(eval_RPN(["4","13","5","/","+"]))
# >>6

print(eval_RPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
# >>22

print(eval_RPN(["4","-2","/","2","-3","-","-"]))
# >>-8