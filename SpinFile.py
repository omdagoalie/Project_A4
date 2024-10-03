# Comp 1020
# 10/01/2024
# Om Soni
# Project A4
# https://github.com/omdagoalie/Project_A4.git
# Kinda forgot about GitHub so It doesn't have multiple pushes

from Spinner import *

# Make Main function
def main():
    spinner = Spinner("synonyms-simplified.txt")
    # Open file
    with open('essay.txt', 'r') as file:
        read_text = file.read().lower()
# printing Original and Options text
    print("Original: ", read_text)

# Loop 3 times for option 1-3
    for i in range(3):
        spun = spinner.spinnn(read_text)
        print(f"Option {i + 1}: ", spun)
        # i + 1 its starting from zero

if __name__ == "__main__":
    main()