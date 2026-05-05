"""
Script Name : main.py
Description : CLI program
Author      : @tonybnya
"""

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        contents = f.read()
    return contents


def main() -> None:
    FILE: str = './books/frankenstein.txt'
    print(get_book_text(FILE))


if __name__ == '__main__':
    main()
