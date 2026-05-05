"""
Script Name : stats.py
Description : Helper functions
Author      : @tonybnya
"""


def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        text = f.read()
    return text


def get_num_words(text: str) -> str:
    num_words: int = len(text.split())
    return f'Found {num_words} total words'


def get_num_chars(text: str) -> dict[str, int]:
    chars: dict[str, int] = {}
    for c in text:
        chars[c.lower()] = chars.get(c.lower(), 0) + 1
    return chars


def sort_on(items: dict[str, int | str]) -> int:
    return items["num"]


def sort_list_dict(chars: dict[str, int]) -> list:
    list_dict: list[dict[str, int | str]] = []
    for k, v in chars.items():
        list_dict.append({"char": k, "num": v})
    list_dict.sort(reverse=True, key=sort_on)
    return list_dict
