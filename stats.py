def get_num_of_words(texts):
    num_of_words = 0
    for text in texts.split():
        num_of_words += 1
    return num_of_words

def get_num_of_chars(texts):
    counts = {}
    char_count_dict = dict()
    for text in texts.lower():
        if text.isalpha():
            counts[text] = counts.get(text, 0) + 1
    return counts

def sort_char_count(counts):
    # 1. start with an empty list
    # 2. for each (char, num) in counts.items():
    #       build {"char": char, "num": num}
    #       add it to the list
    # 3. sort that list with .sort(reverse=True, key=sort_on)
    # 4. return the list

    char_count_list = []
    for char, num in counts.items():
        entry = {"char": char, "num":num}
        char_count_list.append(entry)
    return char_count_list
