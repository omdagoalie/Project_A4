# Comp 1020
# 10/01/2024
# Om Soni
# Project A4
from Spinner import *

def main():
    spinner = Spinner("synonyms-simplified.txt")
    with open('essay.txt', 'r') as file:
        read_text = file.read().lower()

    print("Original: ", read_text)


    for i in range(3):
        spun = spinner.spinnn(read_text)
        print(f"Option {i + 1}: ", spun)


if __name__ == "__main__":
    main()