def main():
    path = 'books/frankenstein.txt'
    text = get_text_from_file(path)
    words = get_word_count(text)
    list = convert_dict(get_letters(text))
    list.sort(reverse=True, key=sort_on)
    print(f"Report for the file {path}")
    print("------------------------------")
    print(f"{words} words in the document")
    for entry in list:
        print(f"{entry["letter"]}: {entry["num"]}")


def get_text_from_file(file):
    with open(file) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def get_letters(text):
    letters = {}
    lower_case_text = text.lower()
    for letter in lower_case_text:
        if letter.isalpha():
            if letter in letters:
                letters[letter] += 1
            else: 
                letters[letter] = 1
    return letters;

def sort_on(dict):
    return dict["num"]

def convert_dict(dict):
    list = []
    for key in dict:
        list.append({"letter": key, "num": dict[key]})
    return list



if __name__ == '__main__':
    main()