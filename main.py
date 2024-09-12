def count_words(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
        words = content.split()
    return len(words)

def letters_to_dict(file_path):
    with open(file_path, 'r') as f:
        content = f.read().lower()
    letters_dict = {}
    for char in content:
        if is_alpha(char):
            letters_dict[char] = letters_dict.get(char, 0) + 1
    return letters_dict

def is_alpha(char):
    return char.isalpha()

def sort_on(item):
    return item[1]

def main():
    file_path = 'books/frankenstein.txt'
    word_count = count_words(file_path)
    letters_dict = letters_to_dict(file_path)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    sorted_letters = sorted(letters_dict.items(), key=sort_on, reverse=True)
    for letter, count in sorted_letters:
        print(f"The '{letter}' character was found {count} times")
    print("--- End report ---")

if __name__ == "__main__":
    main()
