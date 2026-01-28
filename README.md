# Indefinite Integral Calculator
A standalone Python-based calculator for solving indefinite integrals, including support for integration by parts and more advanced integration techniques.

## Requirements

- Python 3.6 or higher
- SymPy library

## Installation

1. Install SymPy (only dependency needed):
```bash
pip install sympy
```

2. Run the calculator:
```bash
python3 integral_calculator.py
```

## How to use

### Basic Usage

When you run the program, you'll see a prompt:
```
Enter integrand (∫ ___ dx):
```

Simply enter your expression and press Enter.

### Syntax

Use standard Python mathematical notation:

| Math Notation | Python Syntax | Example |
|---------------|---------------|---------|
| x² | `x**2` | `x**2 + 3*x + 1` |
| eˣ | `exp(x)` | `exp(x)` |
| ln(x) | `log(x)` | `log(x)` |
| sin(x), cos(x) | `sin(x)`, `cos(x)` | `sin(x)` |
| √x | `sqrt(x)` | `sqrt(x)` |
| x·sin(x) | `x*sin(x)` | `x*sin(x)` |

### Commands

- `help` - Show detailed usage instructions
- `examples` - Browse and select from example problems
- `quit` or `exit` - Exit the calculator


## How It Works

1. **Parsing**: Converts your input into a symbolic expression using SymPy.
2. **Analysis**: Checks if integration by parts or other special techniques are needed.
3. **Integration**: Solves the indefinite integral symbolically.
4. **Verification**: Takes the derivative of the result to check the solution.
5. **Explanation**: Shows the result with steps when possible.

## Technical Details

- **Library**: SymPy (Python symbolic mathematics library)
- **Method**: Symbolic integration with automatic technique selection
- **Verification**: Automatic derivative checking
- **No network required**: Runs completely offline

## License

Free to use and modify.
