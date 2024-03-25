import sys

def count_lines_of_code(file_path):
    try:
        with open(file_path, 'r') as file:
            code_lines = 0

            for line in file:
                line = line.strip()

                if not line or line.startswith('#'):
                    continue

                code_lines += 1

            return code_lines

    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python count_lines.py <filename.py>")
        sys.exit(1)

    file_path = sys.argv[1]
    if not file_path.endswith('.py'):
        print("Error: Please specify a Python file.")
        sys.exit(1)

    lines_of_code = count_lines_of_code(file_path)
    print("Number of lines of code (excluding comments and blank lines):", lines_of_code)
