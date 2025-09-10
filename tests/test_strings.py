import pytest
from textlib import reverse, count_vowels, is_palindrome, to_upper, concat

# ---------------- reverse ----------------
@pytest.mark.parametrize("inp,expected", [
    ("hola", "aloh"),          # happy 1
    ("A b", "b A"),            # happy 2
    ("", ""),                  # borde válido (cadena vacía = happy)
])
def test_reverse_happy(inp, expected):
    assert reverse(inp) == expected

def test_reverse_error_type():
    with pytest.raises(TypeError):
        reverse(None)  # error: no es str

# ---------------- count_vowels ----------------
@pytest.mark.parametrize("inp,expected", [
    ("hola", 2),               # happy 1
    ("HOLA", 2),               # happy 2 (mayúsculas)
    ("xyz", 0),                # borde válido (sin vocales)
])
def test_count_vowels_happy(inp, expected):
    assert count_vowels(inp) == expected

def test_count_vowels_error_type():
    with pytest.raises(TypeError):
        count_vowels(123)  # error: no es str

# ---------------- is_palindrome ----------------
@pytest.mark.parametrize("inp,expected", [
    ("ana", True),                         # happy 1
    ("Anita lava la tina", True),          # happy 2 (espacios/casos)
    ("No 'x' in Nixon", True),             # happy 3 (puntuación/mixto)
    ("abc", False),                        # happy 4 (no palíndromo)
])
def test_is_palindrome_happy(inp, expected):
    assert is_palindrome(inp) == expected

def test_is_palindrome_error_type():
    with pytest.raises(TypeError):
        is_palindrome(['a'])  # error: no es str

# ---------------- to_upper ----------------
@pytest.mark.parametrize("inp,expected", [
    ("hola", "HOLA"),          # happy 1
    ("Ya MiXtO", "YA MIXTO"),  # happy 2
    ("", ""),                  # borde válido
])
def test_to_upper_happy(inp, expected):
    assert to_upper(inp) == expected

def test_to_upper_error_type():
    with pytest.raises(TypeError):
        to_upper(3.14)  # error: no es str

# ---------------- concat ----------------
@pytest.mark.parametrize("a,b,expected", [
    ("hola", "mundo", "holamundo"),  # happy 1
    ("", "x", "x"),                  # happy 2 (cadena vacía)
    ("pre", "", "pre"),              # borde válido
])
def test_concat_happy(a, b, expected):
    assert concat(a, b) == expected

@pytest.mark.parametrize("a,b", [
    (None, "x"),   # error 1
    ("x", 1),      # error 2
])
def test_concat_errors(a, b):
    with pytest.raises(TypeError):
        concat(a, b)
