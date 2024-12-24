# cli_with_args.py
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python cli_with_args.py <name>")
        return

    name = sys.argv[1]
    print(f"Hello, {name}! Welcome to the Python CLI.")

if __name__ == "__main__":
    main()
