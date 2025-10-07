def get_book_text(path_to_file):
    """It takes a file path as input and returns the contents of the file as a string"""
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


def count_words(text):
    "Counts the number of words in a string"
    text = text.split()
    return len(text)


def main():
    path_to_file = "./books/frankenstein.txt"
    text = get_book_text(path_to_file)
    num_words = count_words(text=text)
    print(f"Found {num_words} total words")


main()
