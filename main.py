import RPN
import InfixToPostfix
import numbers_gen

Postfix = InfixToPostfix.ToPostfix()
rpn = RPN.RPN()
num_gen = numbers_gen.AI_Digit()

# Generate numbers for expression (quantity can vary)
(num1, num2, num3, num4) = (num_gen.spit_num(5), num_gen.spit_num(4), num_gen.spit_num(4), num_gen.spit_num(2))

# Building expression to process
expression = "{} - ( {} + {} ) / {}".format(num1, num2, num3, num4)
print(f"Expression: {expression}")

# Transfer regular expression to postfix
postExpression = Postfix.toPostfix(expression)

# Read postfix expression with RPN and do math
afterRPN = rpn.eval(postExpression)

print(afterRPN)
