class Parser:
    def __init__(self, expression):
        self.expression = expression

    def parse(self):
        return f"AST({self.expression})"
