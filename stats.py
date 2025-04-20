def count_words(text):
    list_of_words = text.split()
    count = len(list_of_words)
    return count

def count_chars(text):
    counter = {}
    for char in text:
        lower_char = char.lower()
        if lower_char not in counter:
            counter[lower_char] = 0
        counter[lower_char] += 1
    return counter


def sort_counts(my_dict):
    sorted_dict = dict(sorted(my_dict.items(),reverse=True, key=lambda item: item[1]))
    list = []
    for key, value in sorted_dict.items():
        if key.isalpha() == True:
            output = f"{key}: {value}"
            list.append(output)
    return list
    