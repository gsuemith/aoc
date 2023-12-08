import re

DIGITS_AS_WORDS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def run():
    digits_map = {word:digit for word,digit in zip(DIGITS_AS_WORDS, range(1,10))}
    dt = DigitTrie(digits_map)

    with open("input.txt", "r") as f:
        lines = f.readlines()

    # dt.find_digits(lines[0])

    total = 0
    for line in lines:
        word_digits = dt.find_digits(line)
        
        if word_digits:
            line = line.replace(word_digits[0][1], word_digits[0][0] + word_digits[0][1], 1)
            line = line.replace(word_digits[-1][1], word_digits[-1][1] + word_digits[-1][0])

        digits = re.sub(r"\D", "", line)
        total += int(digits[0] + digits[-1])

    print(total)



class DigitTrie:
    trie = {}
    def __init__(self, digits_map: dict[str, int]):
        self.digits_map = digits_map
        self.build_trie()

    def build_trie(self):
        for word, digit in self.digits_map.items():
            node = self.trie
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]

            node['*'] = (str(digit), word)

    def find_digits(self, line: str):
        found_digits = []
        for i in range(len(line)):
            node = self.trie
            j = i
            while line[j] in node and j < len(line):
                node = node[line[j]]
                j += 1
                if '*' in node:
                    found_digits.append(node['*'])

        return found_digits
    

if __name__ == "__main__":
    run()