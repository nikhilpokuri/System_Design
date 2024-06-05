from abc import ABC, abstractmethod


class Expression(ABC):
    @abstractmethod
    def interpret(self):
        pass


class Number(Expression):
    """Terminal Expression"""

    def __init__(self, number):
        self.number = number

    def interpret(self):
        return self.number


class Add(Expression):
    """Non Terminal Expression to add it's left and right sub expressions"""

    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() + self.right.interpret()


class Subtract(Expression):
    """Non Terminal Expression to subtract it's left and right sub expressions"""

    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() - self.right.interpret()


class Multiply(Expression):
    """Non Terminal Expression to multiply it's left and right sub expressions"""

    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() * self.right.interpret()


class Divide(Expression):
    """Non Terminal Expression to divide it's left and right sub expressions"""

    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() / self.right.interpret()


# client
res = Subtract(Multiply(Number(10), Number(20)), Add(Number(10), Number(20)))
print(res.interpret())
