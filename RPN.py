from keras.models import load_model
import numpy as np


class RPN:

    mul_ = load_model('mul_model')
    sub_ = load_model('sub_model')
    div_ = load_model('div_model')
    add_ = load_model('add_model')

    ops = {
        "+": (lambda self, a, b: self.add_operation(a, b)),
        "-": (lambda self, a, b: self.sub_operation(a, b)),
        "*": (lambda self, a, b: self.mul_operation(a, b)),
        "/": (lambda self, a, b: self.div_operation(a, b))
    }

    def mul_operation(self, a, b):
        return np.exp(self.mul_.predict(np.asarray([np.log(a), np.log(b)]).astype('float32').reshape(-1, 1).T))

    def sub_operation(self, a, b):
        return self.sub_.predict(np.asarray([np.array(a), np.array(b)]).astype('float32').reshape(-1, 1).T)

    def div_operation(self, a, b):
        return np.exp(self.div_.predict(np.asarray([np.log(a), np.log(b)]).astype('float32').reshape(-1, 1).T))

    def add_operation(self, a, b):
        return self.add_.predict(np.asarray([np.array(a), np.array(b)]).astype('float32').reshape(-1, 1).T)


    def eval(self, expression):
        tokens = expression.split()
        stack = []

        for token in tokens:
            if token in self.ops:
                arg2 = stack.pop()
                arg1 = stack.pop()
                result = self.ops[token](self, arg1, arg2)
                stack.append(result)
            else:
                stack.append(int(token))

        return stack.pop()

