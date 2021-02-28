# Stack class
class Stack:
    def __init__(self, size):
        self.stack = []
        self.size = size

    def push(self, item):
        if len(self.stack) < self.size:
            self.stack.append(item)

    def pop(self):
        result = -1

        if self.stack:
            result = self.stack.pop()

        return result

    def display(self):
        if not self.stack:
            print("Stack is empty!")
        else:
            print("Stack data:")
            for item in reversed(self.stack):
                print(item)

    def isEmpty(self):
        return self.stack == []

    def topChar(self):
        result = -1

        if self.stack:
            result = self.stack[len(self.stack) - 1]

        return result


# To postfix class converter
class ToPostfix:
    operands = "0123456789"
    operators = "+-*/^"

    def isOperand(self, c):
        return c in self.operands

    def isOperator(self, c):
        return c in self.operators

    def getPrecedence(self, c):
        result = 0
        for char in self.operators:
            result += 1
            if char == c:
                if c in '-/':
                    result -= 1
                break
        return result

    # infix to postfix
    def toPostfix(self, expression):
        result = ""

        stack = Stack(15)

        for char in expression:
            if self.isOperand(char):
                result += char + " "
            elif self.isOperator(char):
                while True:
                    topChar = stack.topChar()

                    if stack.isEmpty() or topChar == '(':
                        stack.push(char)
                        break
                    else:
                        pC = self.getPrecedence(char)
                        pTC = self.getPrecedence(topChar)

                        if pC > pTC:
                            stack.push(char)
                            break
                        else:
                            result += stack.pop() + " "

            elif char == '(':
                stack.push(char)
            elif char == ')':
                cpop = stack.pop()

                while cpop != '(':
                    result += cpop + " "
                    cpop = stack.pop()

        while not stack.isEmpty():
            cpop = stack.pop()
            result += cpop + " "

        return result
