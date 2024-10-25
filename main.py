def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = count_characters(text)
    print(text)
    print(num_words)
    print(char_count)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    character_count = {}
    for words in text.lower().split():
        for characters in words:
            if characters in character_count:
                character_count[characters] += 1
            else:
                character_count[characters] = 1             

    return dict

main()