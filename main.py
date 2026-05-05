"""
Script Name : main.py
Description : Entry point of the CLI
Author      : @tonybnya
"""

from stats import get_book_text, get_num_chars, get_num_words


def main() -> None:
    FILE: str = './books/frankenstein.txt'
    contents: str = get_book_text(FILE)
    chars: dict[str, int] = get_num_chars(contents)
    print(get_num_words(contents))
    print(chars)


if __name__ == '__main__':
    main()
