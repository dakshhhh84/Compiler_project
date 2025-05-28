import tkinter as tk
from tkinter import messagebox, scrolledtext
from lexer import Lexer
from analyzer import Analyzer
from parser import Parser
from codegenerator import CodeGenerator
from evaluator import Evaluator

class MiniCompilerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini Compiler - Arithmetic Evaluator")
        self.root.geometry("500x500")
        self.root.configure(bg='#f0f4ff')

        self.label = tk.Label(root, text="Enter Arithmetic Expression:", font=("Helvetica", 14), bg='#f0f4ff')
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, font=("Helvetica", 14), width=35, bd=3)
        self.entry.pack(pady=5)

        self.eval_button = tk.Button(root, text="Evaluate", font=("Helvetica", 12, "bold"), bg="#6c63ff", fg="white",
                                     command=self.evaluate_expression)
        self.eval_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Helvetica", 14), fg="green", bg='#f0f4ff')
        self.result_label.pack(pady=10)

        self.log_label = tk.Label(root, text="Compilation Log:", font=("Helvetica", 12), bg='#f0f4ff')
        self.log_label.pack(pady=5)

        self.log_output = scrolledtext.ScrolledText(root, font=("Courier", 10), width=55, height=10, wrap=tk.WORD, state='disabled')
        self.log_output.pack(pady=10)

    def log(self, message):
        self.log_output.config(state='normal')
        self.log_output.insert(tk.END, message + "\n")
        self.log_output.config(state='disabled')
        self.log_output.yview(tk.END)

    def evaluate_expression(self):
        self.log_output.config(state='normal')
        self.log_output.delete(1.0, tk.END)
        self.log_output.config(state='disabled')
        self.result_label.config(text="")

        expression = self.entry.get()
        try:
            self.log("Lexical Analysis...")
            lexer = Lexer(expression)
            tokens = lexer.tokenize()
            self.log(f"Tokens: {tokens}")

            self.log("Syntax Analysis...")
            analyzer = Analyzer(tokens)
            analyzer.analyze()
            self.log("Syntax OK")

            self.log("Parsing...")
            parser = Parser(tokens)
            ast = parser.parse()
            self.log(f"AST: {ast}")

            self.log("Code Generation...")
            generator = CodeGenerator(ast)
            code = generator.generate()
            self.log(f"Generated Code: {code}")

            self.log("Evaluating...")
            evaluator = Evaluator(code)
            result = evaluator.evaluate()

            self.result_label.config(text=f"Result: {result}", fg="green")
            self.log(f"Evaluation Result: {result}")
        except Exception as e:
            self.result_label.config(text="", fg="red")
            messagebox.showerror("Error", str(e))
            self.log(f"Error: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = MiniCompilerApp(root)
    root.mainloop()