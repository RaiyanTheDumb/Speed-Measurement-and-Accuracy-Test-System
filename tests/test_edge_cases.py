import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

from app.calculator import calculate_wpm, calculate_accuracy, calculate_errors


def test_extra_characters():
    # User types more than sample text
    sample = "hello world"
    typed = "hello worlddddd"
    errors = calculate_errors(sample, typed)
    assert errors > 0
    print(f"✅ Extra characters handled: {errors} errors")


def test_short_typed():
    # User types less than sample text
    sample = "hello world"
    typed = "hello"
    accuracy = calculate_accuracy(sample, typed)
    assert accuracy < 100
    print(f"✅ Short typed handled: {accuracy}%")


def test_special_characters():
    # Sample text with punctuation
    sample = "Hello, World!"
    typed = "Hello, World!"
    result = calculate_accuracy(sample, typed)
    assert result == 100
    print(f"✅ Special characters handled: {result}%")


def test_spaces():
    # Spaces counted correctly
    sample = "hi there"
    typed = "hi there"
    errors = calculate_errors(sample, typed)
    assert errors == 0
    print(f"✅ Spaces handled: {errors} errors")


def test_very_fast_typing():
    # 1 second typing time
    result = calculate_wpm("hello world test", 1)
    assert result > 0
    print(f"✅ Very fast typing handled: {result} WPM")


def test_very_slow_typing():
    # 300 seconds typing time
    result = calculate_wpm("hello", 300)
    assert result >= 0
    print(f"✅ Very slow typing handled: {result} WPM")


if __name__ == '__main__':
    test_extra_characters()
    test_short_typed()
    test_special_characters()
    test_spaces()
    test_very_fast_typing()
    test_very_slow_typing()
    print("\n✅ All edge case tests passed!")