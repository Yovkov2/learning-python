import csv
import base64
from pathlib import Path

VAULT = Path(__file__).with_name("vault.csv")

# Global toggle for base64 obfuscation
MASK_PASSWORDS = False

def set_mask(on: bool) -> None:
    global MASK_PASSWORDS
    MASK_PASSWORDS = on
    print(f"Masking is now {'ON' if MASK_PASSWORDS else 'OFF'}.\n")

def ensure_vault() -> None:
    """Create CSV header if file does not exist."""
    if not VAULT.exists():
        with VAULT.open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["site", "username", "password"])

def encode_pwd(p: str) -> str:
    """Return password encoded in base64 if masking is ON, else raw."""
    if not MASK_PASSWORDS:
        return p
    return base64.b64encode(p.encode("utf-8")).decode("utf-8")

def decode_pwd(p: str) -> str:
    """Decode base64 password when masking is ON; otherwise return as-is."""
    if not MASK_PASSWORDS:
        return p
    try:
        return base64.b64decode(p.encode("utf-8")).decode("utf-8")
    except Exception:
        # If not valid base64, just show raw (for legacy rows)
        return p

def add_entry() -> None:
    """Prompt user for credentials and append to CSV."""
    site = input("Site: ").strip()
    user = input("Username: ").strip()
    pwd  = input("Password: ").strip()

    if not site or not user or not pwd:
        print("❌ All fields are required.\n")
        return

    ensure_vault()
    with VAULT.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([site, user, encode_pwd(pwd)])

    print("✅ Saved!\n")

def show_entries() -> None:
    """Read CSV and print all rows."""
    if not VAULT.exists():
        print("No entries yet. Use 'add' to create one.\n")
        return

    with VAULT.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    if not rows:
        print("No entries yet. Use 'add' to create one.\n")
        return

    print("\n🔎 Stored credentials:")
    print("-" * 50)
    for i, row in enumerate(rows, start=1):
        site = row["site"]
        user = row["username"]
        pwd  = decode_pwd(row["password"])
        print(f"{i}. {site:20} | {user:15} | {pwd}")
    print("-" * 50 + "\n")

def main():
    print("🔐 Password Manager")
    print("Commands: add | show | mask on | mask off | quit\n")

    while True:
        cmd = input("> ").strip().lower()

        if cmd == "quit":
            print("Bye! 👋")
            break
        elif cmd == "add":
            add_entry()
        elif cmd == "show":
            show_entries()
        elif cmd == "mask on":
            set_mask(True)
        elif cmd == "mask off":
            set_mask(False)
        else:
            print("Unknown command. Use: add | show | mask on | mask off | quit\n")

if __name__ == "__main__":
    main()
