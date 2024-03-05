from unittest import TestCase

from corn_flakes import number_of_letters_and_digits, upper


class Test(TestCase):
    def test_count_numbers_and_letters(self):
        sentence = "hello world! 123"
        sentence1 = "my sikiru is a good boy 123"
        self.assertEqual("LETTERS10 Digit3",number_of_letters_and_digits.count_numbers_and_letters(sentence))
        self.assertEqual("LETTERS18 Digit3", number_of_letters_and_digits.count_numbers_and_letters(sentence1))

    def test_upper(self):
        sentence = "Hello world!"
        sentence1 = "MR sikiru"
        self.assertEqual("UPPER CASE1 lower case9",upper.counter(sentence))
        self.assertEqual("UPPER CASE2 lower case6",upper.counter(sentence1))



