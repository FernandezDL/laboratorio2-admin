def test_reverse_trampa():
    # reverse("abc") NO es "abc"
    from textlib import reverse
    assert reverse("abc") == "cba"
