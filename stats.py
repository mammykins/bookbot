def count_words(text):
    "Counts the number of words in a string"
    text = text.split()
    return len(text)


def count_characters(text):
    "Counts the number of characters in a string"
    char_count = {}

    for character in text:
        lower_char = character.lower()

        if lower_char in char_count:
            char_count[lower_char] += 1
        else:
            char_count[lower_char] = 1

    return char_count


def sort_characters(dictionary):
    "Sorts the characters in a dictionary by their frequency"
    return dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
