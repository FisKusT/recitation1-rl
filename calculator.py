import tkinter as tk
from tkinter import messagebox
from logic import CalculatorLogic
import math

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GUI Calculator")
        self.root.geometry("450x650")
        self.root.resizable(False, False)
        
        self.logic = CalculatorLogic()
        self.current_input = ""
        
        # Colors & Styling
        self.bg_color = "#121212"
        self.text_color = "#FFFFFF"
        self.btn_digit = "#333333"
        self.btn_operator = "#FF9500"
        self.btn_func = "#A5A5A5"
        
        self.root.configure(bg=self.bg_color)
        
        self._setup_ui()
        self._bind_keys()

    def _setup_ui(self):
        # Display Entry
        self.display = tk.Entry(self.root, font=("Helvetica", 32), justify="right",
                                bd=0, bg=self.bg_color, fg=self.text_color, insertbackground=self.text_color)
        self.display.pack(pady=(40, 20), padx=20, fill="x")
        
        # History Panel (brief view)
        self.history_label = tk.Label(self.root, text="History", font=("Helvetica", 10, "bold"),
                                     bg=self.bg_color, fg="#888888")
        self.history_label.pack(anchor="w", padx=20)
        
        self.history_list = tk.Listbox(self.root, height=3, font=("Helvetica", 10),
                                      bg=self.bg_color, fg="#888888", bd=0, highlightthickness=0)
        self.history_list.pack(fill="x", padx=20, pady=(0, 20))

        # Buttons Grid
        btn_frame = tk.Frame(self.root, bg=self.bg_color)
        btn_frame.pack(expand=True, fill="both", padx=10, pady=10)

        buttons = [
            ('(', ')', 'x²', '^'),
            ('C', '√', '1/x', '/'),
            ('7', '8', '9', '*'),
            ('4', '5', '6', '-'),
            ('1', '2', '3', '+'),
            ('0', '.', 'DEL', '=')
        ]

        for r, row in enumerate(buttons):
            for c, char in enumerate(row):
                btn_color = self.btn_digit
                fg_color = self.text_color
                
                if char in ('/', '*', '-', '+', '='):
                    btn_color = self.btn_operator
                elif char in ('(', ')', 'x²', '^', 'C', '√', '1/x', 'DEL'):
                    btn_color = self.btn_func
                    fg_color = "#000000"

                btn = tk.Button(btn_frame, text=char, font=("Helvetica", 18, "bold"),
                               bg=btn_color, fg=fg_color, width=5, height=2,
                               bd=0, command=lambda x=char: self._on_button_click(x))
                btn.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")
                
            btn_frame.grid_columnconfigure(c, weight=1)
            btn_frame.grid_rowconfigure(r, weight=1)

    def _bind_keys(self):
        # Map physical keys to calculator functions
        self.root.bind('<Return>', lambda e: self._on_button_click('='))
        self.root.bind('<Escape>', lambda e: self._on_button_click('C'))
        self.root.bind('<BackSpace>', self._on_backspace)
        self.root.bind('(', lambda e: self._on_button_click('('))
        self.root.bind(')', lambda e: self._on_button_click(')'))
        
        for i in range(10):
            self.root.bind(str(i), lambda e, x=i: self._on_button_click(str(x)))
            
        operators = {'+': '+', '-': '-', '*': '*', '/': '/', '^': '^', '.': '.'}
        for key, char in operators.items():
            self.root.bind(key, lambda e, x=char: self._on_button_click(x))

    def _on_backspace(self, event):
        self.current_input = self.current_input[:-1]
        self._update_display()

    def _on_button_click(self, char):
        operators = ('+', '-', '*', '/', '^')
        
        if char == '=':
            self._calculate_result()
        elif char == 'C':
            self.current_input = ""
            self._update_display()
        elif char == 'DEL':
            self.current_input = self.current_input[:-1]
            self._update_display()
        elif char == '1/x':
            self.current_input = f"1/({self.current_input})" if self.current_input else ""
            self._update_display()
        elif char == 'x²':
            self.current_input = f"({self.current_input})^2" if self.current_input else ""
            self._update_display()
        elif char == '√':
            self.current_input = f"math.sqrt({self.current_input})" if self.current_input else "math.sqrt("
            self._update_display()
        else:
            # Input validation: Prevent consecutive operators
            if char in operators and self.current_input.endswith(operators):
                # Replace last operator with the new one
                self.current_input = self.current_input[:-1] + str(char)
            else:
                self.current_input += str(char)
            self._update_display()

    def _calculate_result(self):
        if not self.current_input:
            return
            
        result = self.logic.calculate(self.current_input)
        self.current_input = str(result)
        self._update_display()
        self._refresh_history()

    def _update_display(self):
        # Display cleanup for user-friendliness
        display_text = self.current_input.replace('math.sqrt', '√')
        self.display.delete(0, tk.END)
        self.display.insert(0, display_text)

    def _refresh_history(self):
        self.history_list.delete(0, tk.END)
        for item in self.logic.get_history():
            self.history_list.insert(tk.END, item)
        self.history_list.yview(tk.END) # Scroll to bottom

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
