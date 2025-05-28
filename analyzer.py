class Analyzer:
    def __init__(self, expression):
        self.expression = expression

    def analyze(self):
        parentheses = 0
        for char in self.expression:
            if char == '(': parentheses += 1
            elif char == ')': parentheses -= 1
            if parentheses < 0:
                raise ValueError("Mismatched parentheses")
        if parentheses != 0:
            raise ValueError("Mismatched parentheses")
        return True