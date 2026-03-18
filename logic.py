import math

class CalculatorLogic:
    def __init__(self):
        self.memory = 0
        self.history = []

    def calculate(self, expression):
        try:
            # Safely evaluate the mathematical expression
            # Note: In a production app, a custom parser is safer than eval()
            # but for this desktop utility, we'll use a controlled eval with a limited scope.
            
            # Replace user-friendly symbols with Python operators
            processed_expr = expression.replace('^', '**').replace('√', 'math.sqrt')
            
            # Auto-close parentheses if they are missing
            open_parens = processed_expr.count('(')
            close_parens = processed_expr.count(')')
            if open_parens > close_parens:
                processed_expr += ')' * (open_parens - close_parens)
            
            # Use a restricted global/local environment for eval
            safe_dict = {"math": math, "__builtins__": {}}
            result = eval(processed_expr, safe_dict)
            
            # Formatting result to avoid trailing zeros for integers
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            
            self.history.append(f"{expression} = {result}")
            return result
        except ZeroDivisionError:
            return "Error: Div by 0"
        except Exception:
            return "Error"

    def get_history(self):
        return self.history[-10:] # Return last 10 entries
