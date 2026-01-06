import sys
from stats import get_num_of_words, get_num_of_chars, sort_char_count

def get_book_text(pathfile):
    with open(pathfile) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) == 2:
        pathfile = sys.argv[1]
        texts = get_book_text(pathfile)
        num_of_words = get_num_of_words(texts)
        counts = get_num_of_chars(texts)
        sorted_char_count = sort_char_count(counts)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {pathfile}...")
        print("----------- Word Count ----------")
        print(f"Found {num_of_words} total words")
        print("--------- Character Count -------")
        for item in sorted_char_count:
            print(f"{item['char']}: {item['num']}")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()
