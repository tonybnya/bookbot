"""
Script Name : main.py
Description : CLI program
Author      : @tonybnya
"""

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        contents = f.read()
    return contents


def count_words(contents: str) -> str:
    num_words: int = len(contents.split())
    return f'Found {num_words} total words'


def main() -> None:
    FILE: str = './books/frankenstein.txt'
    # print(get_book_text(FILE))
    contents: str = get_book_text(FILE)
    print(count_words(contents))


if __name__ == '__main__':
    main()
