"""
Script Name : stats.py
Description : Helper functions
Author      : @tonybnya
"""


def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        contents = f.read()
    return contents


def get_num_words(contents: str) -> str:
    num_words: int = len(contents.split())
    return f'Found {num_words} total words'
