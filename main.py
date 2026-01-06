import sys
from stats import get_num_of_words, get_num_of_words_count, sort_word_count

def get_book_text(pathfile):
    with open(pathfile) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) == 2:
        pathfile = sys.argv[1]
        texts = get_book_text(pathfile)
        num_of_words = get_num_of_words(texts)
        word_counts = get_num_of_words_count(texts)
        sorted_word_count = sort_word_count(word_counts)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {pathfile}...")
        print("----------- Word Count ----------")
        print(f"Found {num_of_words} total words")
        print("--------- Top 20 Words ---------")
        for item in sorted_word_count[:20]:
            print(f"{item['word']}: {item['num']}")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()
