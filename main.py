from stats import count_words
from stats import count_characters
from stats import sort_characters


def get_book_text(path_to_file):
    """It takes a file path as input and returns the contents of the file as a string"""
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


def main():
    path_to_file = "./books/frankenstein.txt"
    text = get_book_text(path_to_file)
    num_words = count_words(text=text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sorted_dictionary = sort_characters(count_characters(text=text))
    for char, count in sorted_dictionary.items():
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")


main()
