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
