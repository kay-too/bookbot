def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = count_characters(text)
    char_sorted_list = chars_dict_sort(char_count)
    print("Beginning Report of books/frankestein.txt")
    print(f"{num_words} words found in the document")
    print()

    for item in char_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' charcter was found {item['num']} times")

    print("End Report")

def get_num_words(text):
    words = text.split()
    return len(words)

def sort_on(d):
    return d["num"]

def chars_dict_sort(num_chars_dict):
    sorted_list = []
    for chars in num_chars_dict:
        sorted_list.append({"char": chars, "num": num_chars_dict[chars]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def count_characters(text):
    character_count = {}
    for words in text.lower().split():
        for characters in words:
            if characters in character_count:
                character_count[characters] += 1
            else:
                character_count[characters] = 1             

    return character_count

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()