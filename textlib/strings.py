from typing import Iterable

_VOWELS = set("aeiouAEIOU")

def _ensure_str(*args):
    for a in args:
        if not isinstance(a, str):
            raise TypeError("Se esperaba str")

def reverse(s: str) -> str:
    _ensure_str(s)
    return s[::-1]

def count_vowels(s: str) -> int:
    _ensure_str(s)
    return sum(1 for ch in s if ch in _VOWELS)

def is_palindrome(s: str) -> bool:
    _ensure_str(s)
    # Normalizamos a alfanumérico y minúsculas
    norm = "".join(ch.lower() for ch in s if ch.isalnum())
    return norm == norm[::-1]

def to_upper(s: str) -> str:
    _ensure_str(s)
    return s.upper()

def concat(a: str, b: str) -> str:
    _ensure_str(a, b)
    return a + b
