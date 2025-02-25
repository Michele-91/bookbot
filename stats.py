def count_words(book_text):
    num_words = book_text.split()
    return len(num_words)


def count_characters(book_text):
    chars_dict = {}
    for char in book_text:
        char_lower = char.lower()
        if char_lower not in chars_dict:
            chars_dict[char_lower] = 1
        else:
            chars_dict[char_lower] += 1
    return chars_dict

def sort_on(d):
    return d["num"]

def sort_characters(chars_dict):
    sorted_list = []
    for dict in chars_dict:
        sorted_list.append({"char": dict, "num": chars_dict[dict]})
    sorted_list.sort(reverse=True, key=sort_on)
    # sorted_list.sort(reverse=True, key=lambda d: d["num"])
    return sorted_list

