# GUI Calculator - BIU RL Course Project
# PR example
## a. Objective
The objective of this project is to provide a robust, cross-platform graphical calculator application. It is designed to handle basic arithmetic, advanced mathematical operations (square root, exponentiation, reciprocal), and complex expressions using parentheses, all within a modern, dark-themed user interface.

## b. Installation Guide

### Windows (PowerShell)
1. **Prerequisites:** Ensure Python 3.x is installed (`python --version`).
2. **Clone/Copy:** Navigate to the project directory.
3. **Run:**
   ```powershell
   python calculator.py
   ```

### Linux (Ubuntu/Debian)
1. **Prerequisites:** Install Python and Tkinter (often required separately on Linux):
   ```bash
   sudo apt-get update
   sudo apt-get install python3 python3-tk
   ```
2. **Run:**
   ```bash
   python3 calculator.py
   ```

### Mac OS
1. **Prerequisites:** Python 3 is usually pre-installed. Verify with `python3 --version`.
2. **Run:**
   ```bash
   python3 calculator.py
   ```

## c. User Manual
- **Basic Calculation:** Click digits and operators (`+`, `-`, `*`, `/`) and press `=` or `Enter`.
- **Parentheses:** Use `(` and `)` to group expressions for correct order of operations.
- **Advanced Buttons:**
  - `x²`: Squares the current number.
  - `√`: Calculates the square root (automatically closes parentheses).
  - `^`: General exponentiation (e.g., `2^3` for 2 to the power of 3).
  - `1/x`: Calculates the reciprocal.
- **Correction:**
  - `DEL`: Deletes the last character entered.
  - `C` or `Esc`: Clears the entire display.
- **History:** View the last 10 calculations in the scrollable panel above the keypad.

## d. Config File Description
Currently, the application uses hardcoded styling parameters within `calculator.py` for high performance and zero-dependency portability.
- **bg_color:** `#121212` (Dark background)
- **text_color:** `#FFFFFF` (White text)
- **btn_operator:** `#FF9500` (Orange for math actions)
- **btn_func:** `#A5A5A5` (Grey for utility actions)

## e. File Structure
```text
recitation1_project/
├── calculator.py      # Main GUI Application (Tkinter)
├── logic.py           # Mathematical Engine & History Logic
├── test_logic.py      # Automated Unit Tests
├── PRD.md             # Product Requirements Document
├── TODO.md            # Task Tracking & Progress
└── README.md          # Project Documentation (This file)
```

## f. GUI Picture Examples
*(Note: As a CLI-based agent, I cannot generate image files, but here is a text representation of the layout)*
```text
+-----------------------+
|         History Panel |
+-----------------------+
|               Display |
+-----------------------+
| (  |  ) | x² |  ^     |
| C  |  √ | 1/x|  /     |
| 7  |  8 |  9 |  *     |
| 4  |  5 |  6 |  -     |
| 1  |  2 |  3 |  +     |
| 0  |  . | DEL|  =     |
+-----------------------+
```

## g. Unit Test Explanation
The project includes a dedicated testing suite in `test_logic.py`. These tests verify:
1. **Arithmetic Correctness:** Ensuring `+`, `-`, `*`, `/` yield precise results.
2. **Advanced Math:** Validating `^` (power) and `sqrt` (square root) logic.
3. **Error Resilience:** Checking that division by zero returns "Error: Div by 0" instead of crashing.
4. **History Persistence:** Ensuring calculations are correctly logged.

To run tests: `python test_logic.py`

## h. Copyright & Academic Info
**Project:** Recitation 1 - GUI Calculator  
**Course:** Reinforcement Learning (RL)  
**Institution:** Bar Ilan University (BIU)  
**Student:** Tal Fiskus (208423707)  
**Copyright © 2026.** All rights reserved. Created as part of the BIU RL Course curriculum.
