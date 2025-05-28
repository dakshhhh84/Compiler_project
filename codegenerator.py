class CodeGenerator:
    def __init__(self, ast):
        self.ast = ast

    def generate(self):
        return self.ast.replace("AST(", "").rstrip(")")