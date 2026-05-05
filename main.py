"""
Script Name : main.py
Description : Entry point of the CLI
Author      : @tonybnya
"""

from stats import get_book_text, get_num_words


def main() -> None:
    FILE: str = './books/frankenstein.txt'
    print(get_book_text(FILE))
    contents: str = get_book_text(FILE)
    print(get_num_words(contents))


if __name__ == '__main__':
    main()
