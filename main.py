import sympy as sp
from sympy import symbols, integrate, sin, cos, tan, exp, log, sqrt, atan, asin, acos
from sympy.integrals.manualintegrate import manualintegrate, integral_steps
import sys

def print_header():
    print("=" * 70)
    print(" " * 15 + "INDEFINITE INTEGRAL CALCULATOR")
    print("=" * 70)
    print()

def print_help():
    print("\nHOW TO USE:")
    print("-" * 70)
    print("Enter the expression using standard Python mathematical notation:")
    print("  - Powers: x**2, x**3")
    print("  - Trigonometric: sin(x), cos(x), tan(x)")
    print("  - Exponential: exp(x) for e^x")
    print("  - Logarithm: log(x) for ln(x)")
    print("  - Square root: sqrt(x)")
    print("  - Multiplication: x*sin(x), 2*x")
    print()
    print("EXAMPLES:")
    print("  1. x**2 + 3*x + 1")
    print("  2. x*exp(x)           (integration by parts)")
    print("  3. x*sin(x)           (integration by parts)")
    print("  4. log(x)             (integration by parts)")
    print("  5. exp(x)*sin(x)")
    print("  6. 1/(x**2 + 1)")
    print()
    print("COMMANDS:")
    print("  • 'help' - Show this help message")
    print("  • 'examples' - Load example problems")
    print("  • 'quit' or 'exit' - Exit the calculator")
    print("-" * 70)
    print()

def show_examples():
    examples = [
        ("x**2 + 3*x + 1", "Basic polynomial"),
        ("sin(x)", "Trig function"),
        ("exp(x)", "Exponential function"),
        ("x*exp(x)", "Integration by parts"),
        ("x*sin(x)", "Integration by parts"),
        ("1/(x**2 + 1)", "Inverse trigonometric"),
        ("x*sqrt(x)", "Power rule"),
    ]
    
    print("\nEXAMPLE PROBLEMS:")
    print("-" * 70)
    for i, (expr, desc) in enumerate(examples, 1):
        print(f"{i:2d}. {expr:25s} - {desc}")
    print("-" * 70)
    
    choice = input("\nEnter example number to try (or press Enter to skip): ").strip()
    if choice.isdigit() and 1 <= int(choice) <= len(examples):
        return examples[int(choice) - 1][0]
    return None

def check_integration_by_parts(expr, x):
    # patterns for ibp
    patterns = [
        lambda e: e.has(x * exp(x)),
        lambda e: e.has(x * sin(x)),
        lambda e: e.has(x * cos(x)),
        lambda e: e.has(log(x)),
        lambda e: e.has(x**2 * exp(x)),
        lambda e: e.has(x * log(x)),
        lambda e: e.has(exp(x) * sin(x)),
        lambda e: e.has(exp(x) * cos(x)),
    ]
    
    return any(pattern(expr) for pattern in patterns)

def solve_integral(expression_str):
    x = symbols('x')
    
    try:
        # Parser
        expr = sp.sympify(expression_str)
        
        print(f"\nSOLVING: ∫ ({expr}) dx")
        print("-" * 70)
        
        uses_ibp = check_integration_by_parts(expr, x)
        if uses_ibp:
            print("→ This integral likely requires INTEGRATION BY PARTS")
            print()
        
        # Compute 
        result = integrate(expr, x)
        
        print(f"\nRESULT:")
        print(f"∫ ({expr}) dx = {result} + C")
        print()
        
        try:
            steps = integral_steps(expr, x)
            if steps:
                print("STEPS:")
                print(sp.pretty(steps, use_unicode=True))
                print()
        except:
            # basic explanation
            if uses_ibp:
                print("TECHNIQUE USED: Integration by Parts")
                print("Formula: ∫ u dv = uv - ∫ v du")
                print()
                
                if expr.has(x * exp(x)):
                    print("Suggested choice:")
                    print("  u = x,     dv = exp(x) dx")
                    print("  du = dx,   v = exp(x)")
                elif expr.has(x * sin(x)):
                    print("Suggested choice:")
                    print("  u = x,     dv = sin(x) dx")
                    print("  du = dx,   v = -cos(x)")
                elif expr.has(x * cos(x)):
                    print("Suggested choice:")
                    print("  u = x,     dv = cos(x) dx")
                    print("  du = dx,   v = sin(x)")
                elif expr.has(log(x)):
                    print("Suggested choice:")
                    print("  u = log(x),     dv = dx")
                    print("  du = 1/x dx,    v = x")
                print()
        
        print("VERIFICATION (derivative of result):")
        derivative = sp.diff(result, x)
        simplified = sp.simplify(derivative)
        print(f"d/dx [{result}] = {simplified}")
        
        if sp.simplify(simplified - expr) == 0:
            print("Verified: derivative matches original integrand")
        else:
            print(f"Simplified: {simplified}")
        
        print("-" * 70)
        
    except Exception as e:
        print(f"\nERROR: Could not solve integral")
        print(f"Details: {str(e)}")
        print("Please check your expression syntax.")
        print("Type 'help' for usage instructions.")

def main():
    #Main Looop
    print_header()
    print("Welcome! Type 'help' for instructions, 'examples' for sample problems.")
    print("Type 'quit' or 'exit' to close the calculator.\n")
    
    while True:
        try:
            user_input = input("Enter integrand (∫ ___ dx): ").strip()
            
            if not user_input:
                continue
            
            # Handler
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("\nThank you for using the Indefinite Integral Calculator!")
                break
            elif user_input.lower() == 'help':
                print_help()
                continue
            elif user_input.lower() == 'examples':
                example = show_examples()
                if example:
                    user_input = example
                else:
                    continue
            
            # Solve
            solve_integral(user_input)
            print()
            
        except KeyboardInterrupt:
            print("\n\nThank you for using!")
            break
        except EOFError:
            break

if __name__ == "__main__":
    # Check SymPy 
    try:
        import sympy
    except ImportError:
        print("ERROR: SymPy is required to run this calculator.")
        print("Install it with: pip install sympy")
        sys.exit(1)
    
    main()
