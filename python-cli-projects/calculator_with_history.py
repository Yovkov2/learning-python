import ast
import operator
from pathlib import Path

HISTORY_FILE = Path(__file__).with_name("history.txt")

# Allowed operators mapped to real Python functions
OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}

def safe_eval(expr: str) -> float:
    node = ast.parse(expr, mode="eval")

    def _eval(n):
        if isinstance(n, ast.Expression):
            return _eval(n.body)

        # Literals (int/float)
        if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)):
            return n.value

        # Parenthesized expressions resolve to BinOp/UnaryOp etc.
        if isinstance(n, ast.BinOp) and type(n.op) in OPS:
            left = _eval(n.left)
            right = _eval(n.right)
            return OPS[type(n.op)](left, right)

        if isinstance(n, ast.UnaryOp) and type(n.op) in OPS:
            return OPS[type(n.op)](_eval(n.operand))

        # Disallow everything else
        raise ValueError("Unsupported expression")

    return _eval(node)

def append_history(line: str) -> None:
    """Append a single line to history file."""
    with HISTORY_FILE.open("a", encoding="utf-8") as f:
        f.write(line + "\n")

def read_history(last_n: int = 5) -> list[str]:
    """Return last N lines from history (if file exists)."""
    if not HISTORY_FILE.exists():
        return []
    with HISTORY_FILE.open("r", encoding="utf-8") as f:
        lines = [ln.rstrip("\n") for ln in f]
    return lines[-last_n:]

def clear_history() -> None:
    HISTORY_FILE.write_text("", encoding="utf-8")

def main():
    print("🧮 Calculator with History")
    print("Type a math expression, or commands: history | clear | quit")
    while True:
        expr = input("> ").strip()

        if not expr:
            continue

        if expr.lower() == "quit":
            print("Bye! 👋")
            break

        if expr.lower() == "history":
            lines = read_history(5)
            if lines:
                print("\nLast 5 calculations:")
                for ln in lines:
                    print("  " + ln)
                print()
            else:
                print("No history yet.\n")
            continue

        if expr.lower() == "clear":
            clear_history()
            print("History cleared.\n")
            continue

        # Try to evaluate the expression safely
        try:
            result = safe_eval(expr)
            line = f"{expr} = {result}"
            print(line)
            append_history(line)
        except Exception as e:
            print(f"Error: {e}\nAllowed: numbers, (), + - * / % **")

if __name__ == "__main__":
    main()
