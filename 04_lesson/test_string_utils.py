import pytest
from string_utils import StringUtils

class TestStringUtils:

    def setup_method(self):
        self.utils = StringUtils()

    # Тесты для capitalize
    def test_capitalize_normal(self):
        assert self.utils.capitalize("skypro") == "Skypro"

    def test_capitalize_empty_string(self):
        assert self.utils.capitalize("") == ""

    def test_capitalize_single_char(self):
        assert self.utils.capitalize("a") == "A"

    def test_capitalize_whitespace_only(self):
        assert self.utils.capitalize("   ") == "   "

    def test_capitalize_none(self):
        with pytest.raises(AttributeError):
            self.utils.capitalize(None)

    def test_capitalize_numbers(self):
        assert self.utils.capitalize("123abc") == "123abc"

    # Тесты для trim
    def test_trim_normal(self):
        assert self.utils.trim("   skypro") == "skypro"

    def test_trim_no_spaces(self):
        assert self.utils.trim("skypro") == "skypro"

    def test_trim_only_spaces(self):
        assert self.utils.trim("     ") == ""

    def test_trim_empty_string(self):
        assert self.utils.trim("") == ""

    def test_trim_none(self):
        with pytest.raises(AttributeError):
            self.utils.trim(None)

    def test_trim_tabs(self):
        # Метод не обрабатывает табуляции — это дефект!
        assert self.utils.trim("\t\tskypro") == "\t\tskypro"

    # Тесты для contains
    def test_contains_found(self):
        assert self.utils.contains("SkyPro", "S") is True

    def test_contains_not_found(self):
        assert self.utils.contains("SkyPro", "U") is False

    def test_contains_empty_symbol(self):
        # Поведение Python: пустая строка содержится в любой строке
        assert self.utils.contains("abc", "") is True

    def test_contains_empty_string(self):
        assert self.utils.contains("", "a") is False

    def test_contains_none_string(self):
        with pytest.raises(AttributeError):
            self.utils.contains(None, "a")

    def test_contains_none_symbol(self):
        with pytest.raises(TypeError):
            self.utils.contains("abc", None)

    # Тесты для delete_symbol
    def test_delete_symbol_single_char(self):
        assert self.utils.delete_symbol("SkyPro", "k") == "SyPro"

    def test_delete_symbol_substring(self):
        assert self.utils.delete_symbol("SkyPro", "Pro") == "Sky"

    def test_delete_symbol_not_found(self):
        assert self.utils.delete_symbol("SkyPro", "X") == "SkyPro"

    def test_delete_symbol_empty_symbol(self):
        # replace("", "") не меняет строку
        assert self.utils.delete_symbol("abc", "") == "abc"

    def test_delete_symbol_empty_string(self):
        assert self.utils.delete_symbol("", "a") == ""

    def test_delete_symbol_none_string(self):
        with pytest.raises(AttributeError):
            self.utils.delete_symbol(None, "a")

    def test_delete_symbol_none_symbol(self):
        with pytest.raises(TypeError):
            self.utils.delete_symbol("abc", None)
