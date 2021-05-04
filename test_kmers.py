import pytest
import kmers


class TestClass:
    """
    Multiple tests for kmers in a class
    """
    def test_linguistic_complexity_null_text(self):
        """
        Test if calling linguistic_complexity with null text
        raises ValueError
        :return: None
        """
        with pytest.raises(ValueError):
            kmers.linguistic_complexity(None)

    def test_linguistic_complexity_empty_text(self):
        """
        Test if calling linguistic_complexity with empty text
        raises ValueError
        :return: None
        """
        with pytest.raises(ValueError):
            kmers.linguistic_complexity("")

    def test_linguistic_complexity_valid(self):
        """
        Test if calling linguistic_complexity with valid text
        returns right result
        :return: None
        """
        assert kmers.linguistic_complexity("ATTTGGATT") == 0.875

    def test_count_kmers_null_text(self):
        """
        Test if calling count_kmers with null text
        raises ValueError
        :return: None
        """
        with pytest.raises(ValueError):
            kmers.count_kmers(None, 1)

    def test_count_kmers_empty_text(self):
        """
        Test if calling count_kmers with empty text
        raises ValueError
        :return: None
        """
        with pytest.raises(ValueError):
            kmers.count_kmers("", 1)

    def test_count_kmers_k_not_greater_than_0(self):
        """
        Test if calling count_kmers with k <= 0
        raises ValueError
        :return: None
        """
        with pytest.raises(ValueError):
            kmers.count_kmers("abc", -1)

    def test_count_kmers_k_greater_than_text_length(self):
        """
        Test if calling count_kmers with k > len(self.text)
        raises ValueError
        :return: None
        """
        with pytest.raises(ValueError):
            kmers.count_kmers("abc", 4)

    def test_count_kmers_valid(self):
        """
        Test if calling count_kmers with valid k
        returns right result
        :return: None
        """
        assert kmers.count_kmers("ATTTGGATT", 4) == 6

    def test_possible_kmers_null_text(self):
        """
        Test if calling possible_kmers with null text
        raises ValueError
        :return: None
        """
        with pytest.raises(ValueError):
            kmers.possible_kmers(None, 1)

    def test_possible_kmers_empty_text(self):
        """
        Test if calling possible_kmers with empty text
        raises ValueError
        :return: None
        """
        with pytest.raises(ValueError):
            kmers.possible_kmers("", 1)

    def test_possible_kmers_k_not_greater_than_0(self):
        """
        Test if calling possible_kmers with k <= 0
        raises ValidError
        :return: None
        """
        with pytest.raises(ValueError):
            kmers.possible_kmers("abc", -1)

    def test_possible_kmers_k_greater_than_text_length(self):
        """
        Test if calling possible_kmers with k > len(text)
        raises ValidError
        :return: None
        """
        with pytest.raises(ValueError):
            kmers.possible_kmers("abc", 4)

    def test_possible_kmers_valid(self):
        """
        Test if calling possible_kmers with k <= 0
        raises ValidError
        :return: None
        """
        assert kmers.possible_kmers("ATTTGGATT", 7) == 3