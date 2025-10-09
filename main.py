from stats import count_words
from stats import count_characters


def get_book_text(path_to_file):
    """It takes a file path as input and returns the contents of the file as a string"""
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


def main():
    path_to_file = "./books/frankenstein.txt"
    text = get_book_text(path_to_file)
    num_words = count_words(text=text)
    print(f"Found {num_words} total words")
    print(f"{count_characters(text=text)}")


main()
