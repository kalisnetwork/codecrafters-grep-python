import sys
import re


# import pyparsing - available if you need it!
# import lark - available if you need it!


def match_pattern(input_line, pattern):
    if pattern == r"\w":
        return bool(re.search(r'\w', input_line))
    elif pattern == r"\d":
        return any(c.isdigit() for c in input_line)
    else:
        # Handle literal characters
        return pattern in input_line

def main():
    if len(sys.argv) != 3 or sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)

    pattern = sys.argv[2]
    input_line = sys.stdin.read().strip()

    if match_pattern(input_line, pattern):
        exit(0)
    else:
        exit(1)

if __name__ == "__main__":
    main()