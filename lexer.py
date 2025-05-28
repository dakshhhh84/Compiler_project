class Lexer:
    def __init__(self, expression):
        self.expression = expression

    def tokenize(self):
        if not all(c in "0123456789+-*/(). " for c in self.expression):
            raise ValueError("Invalid characters in expression.")
        return self.expression