class Evaluator:
    def __init__(self, code):
        self.code = code

    def evaluate(self):
        try:
            result = eval(self.code)
            return result
        except Exception as e:
            raise ValueError(f"Evaluation error: {e}")
