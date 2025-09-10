import pytest
from textlib.strings import reverse, count_vowels, is_palindrome, to_upper, concat

# --- reverse ---
@pytest.mark.parametrize("inp,expected", [
    ("hola", "aloh"),
    ("", ""),
    ("A b", "b A"),
])
def test_reverse_happy(inp, expected):
    assert reverse(inp) == expected

def test_reverse_type_error():
    with pytest.raises(TypeError):
        reverse(None)  # type: ignore

# --- count_vowels ---
@pytest.mark.parametrize("inp,expected", [
    ("hola", 2),
    ("HOLA", 2),
    ("xyz", 0),
])
def test_count_vowels_happy(inp, expected):
    assert count_vowels(inp) == expected

def test_count_vowels_type_error():
    with pytest.raises(TypeError):
        count_vowels(123)  # type: ignore

# --- is_palindrome ---
@pytest.mark.parametrize("inp,expected", [
    ("ana", True),
    ("Anita lava la tina", True),
    ("abc", False),
    ("No 'x' in Nixon", True),
])
def test_is_palindrome_happy(inp, expected):
    assert is_palindrome(inp) == expected

def test_is_palindrome_type_error():
    with pytest.raises(TypeError):
        is_palindrome(['a'])  # type: ignore

# --- to_upper ---
@pytest.mark.parametrize("inp,expected", [
    ("hola", "HOLA"),
    ("Ya MiXtO", "YA MIXTO"),
])
def test_to_upper_happy(inp, expected):
    assert to_upper(inp) == expected

def test_to_upper_type_error():
    with pytest.raises(TypeError):
        to_upper(3.14)  # type: ignore

# --- concat ---
@pytest.mark.parametrize("a,b,expected", [
    ("hola", "mundo", "holamundo"),
    ("", "x", "x"),
])
def test_concat_happy(a, b, expected):
    assert concat(a, b) == expected

@pytest.mark.parametrize("a,b", [
    (None, "x"),
    ("x", 1),
])
def test_concat_type_error(a, b):
    with pytest.raises(TypeError):
        concat(a, b)  # type: ignore
