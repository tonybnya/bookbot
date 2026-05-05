"""
Script Name : main.py
Description : Entry point of the CLI
Author      : @tonybnya
"""

import sys
from stats import get_book_text, get_num_chars, get_num_words, sort_list_dict


def main() -> None:
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    book_path: str = sys.argv[1]
    contents: str = get_book_text(book_path)
    chars: dict[str, int] = get_num_chars(contents)
    list_dict: list[dict[str, int | str]] = sort_list_dict(chars)
    print(get_num_words(contents))
    # print(list_dict)
    for d in list_dict:
        print(f'{d["char"]}: {d["num"]}')


if __name__ == '__main__':
    main()
