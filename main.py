from stats import count_words, count_chars, sort_counts
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        text = f.read()
    return text


def main(path):
    text = get_book_text(path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path.lstrip("./")}")
    print("----------- Word Count ----------")
    print(f"Found {count_words(text)} total words")
    print("--------- Character Count -------")
    char_counts = count_chars(text)
    sorted_char_counts = sort_counts(char_counts)
    for char in sorted_char_counts:
        print(char)
    print("============= END ===============")


if len(sys.argv) > 1:
    main(sys.argv[1])
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
