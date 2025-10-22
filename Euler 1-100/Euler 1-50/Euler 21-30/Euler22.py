import os


def txt_reader() -> list[str]:
    names_list = []
    file = "Euler22.txt"
    file_path = os.path.join(os.path.dirname(__file__), file)
    with open(file_path, "r") as f:
        x = f.read()
        x = x.replace('"','')
        names_list = x.split(",")
        names_list.sort()
    return names_list

def alphabet_score(array):
    alphabet = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
    total = 0
    for index,name in enumerate(array):
        letter_total = 0
        for letter in name:
            letter_total += alphabet[letter]
        total += letter_total*(index+1)
    return total
    


def main():
    names_list = txt_reader()
    print(alphabet_score(names_list))



if __name__ == "__main__":
    main()