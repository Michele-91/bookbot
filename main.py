import sys
from stats import ( 
    count_words, 
    count_characters, 
    sort_characters
)


def get_book_test(file_path):
    file_contents = None
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")




def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    # book_path = "./books/frankenstein.txt"
    book_path = sys.argv[1]
    book_text = get_book_test(book_path)
    word_count = count_words(book_text)
    characters_dict = count_characters(book_text)
    sorted_chars_list = sort_characters(characters_dict)
    print_report(book_path, word_count, sorted_chars_list)


main()