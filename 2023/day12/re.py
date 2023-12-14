import re

def run():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    pattern = r"[?\.]*[#?]{1}[?\.]+[#?]{3}[?\.]+[#?]{1}[?\.]*"
    condition = "????#?.???"

    m = re.match(pattern, condition)
    print(m)

if __name__ == "__main__":
    run()