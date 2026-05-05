"""
Script Name : main.py
Description : Entry point of the CLI
Author      : @tonybnya
"""

from stats import get_book_text, get_num_chars, get_num_words, sort_list_dict


def main() -> None:
    FILE: str = './books/frankenstein.txt'
    contents: str = get_book_text(FILE)
    chars: dict[str, int] = get_num_chars(contents)
    list_dict: list[dict[str, int | str]] = sort_list_dict(chars)
    print(get_num_words(contents))
    # print(list_dict)
    for d in list_dict:
        print(f'{d["char"]}: {d["num"]}')


if __name__ == '__main__':
    main()
