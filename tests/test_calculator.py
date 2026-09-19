import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

from app.calculator import (calculate_wpm, calculate_accuracy,
                             calculate_errors, get_typing_level)


def test_wpm_normal():
    # 25 chars in 30 seconds = 10 WPM
    result = calculate_wpm("hello world how are", 30)
    assert result > 0
    print(f"✅ WPM normal: {result}")


def test_wpm_zero_time():
    # Should return 0 not crash
    result = calculate_wpm("hello", 0)
    assert result == 0
    print(f"✅ WPM zero time: {result}")


def test_accuracy_perfect():
    text = "hello world"
    result = calculate_accuracy(text, text)
    assert result == 100
    print(f"✅ Accuracy perfect: {result}%")


def test_accuracy_empty():
    result = calculate_accuracy("hello", "")
    assert result == 0
    print(f"✅ Accuracy empty: {result}%")


def test_accuracy_all_wrong():
    result = calculate_accuracy("hello", "xxxxx")
    assert result == 0
    print(f"✅ Accuracy all wrong: {result}%")


def test_errors_none():
    text = "hello world"
    result = calculate_errors(text, text)
    assert result == 0
    print(f"✅ Errors none: {result}")


def test_errors_some():
    result = calculate_errors("hello", "hxllo")
    assert result == 1
    print(f"✅ Errors some: {result}")


def test_typing_levels():
    assert get_typing_level(20) == 'Beginner'
    assert get_typing_level(40) == 'Average'
    assert get_typing_level(60) == 'Fluent'
    assert get_typing_level(90) == 'Fast'
    assert get_typing_level(120) == 'Expert'
    print("✅ All typing levels correct")


if __name__ == '__main__':
    test_wpm_normal()
    test_wpm_zero_time()
    test_accuracy_perfect()
    test_accuracy_empty()
    test_accuracy_all_wrong()
    test_errors_none()
    test_errors_some()
    test_typing_levels()
    print("\n✅ All tests passed!")