import typing
import unittest


def calc_string(template: str, alphabet: typing.List[str], lex_number: int) -> str:
    template_positions = []
    for index in range(len(template)):
        if template[index] == "?":
            template_positions.append(index)
    lex_number = lex_number - 1
    template_values = []
    for _ in range(len(template_positions)):
        template_values.insert(0, alphabet[lex_number % len(alphabet)])
        lex_number = lex_number // len(alphabet)
    for index in range(len(template_positions)):
        template = template[:template_positions[index]] + template_values[index] + template[template_positions[index] + 1:]
    return template


class TestTaskImplementation(unittest.TestCase):

    def test_example(self):
        self.assertEqual("abdc", calc_string("ab?c", self.__class__.alphabet, 4))

    def test_task1(self):
        self.assertEqual("adecabedeba", calc_string("a??cab?d?ba", self.__class__.alphabet, 500))

    def test_task2(self):
        self.assertEqual("abebbdcbddcbbdebcdbabdadaee", calc_string("?be?bdcb?dcb?debcd??bdad?ee", self.__class__.alphabet, 5151))

    alphabet = ["a", "b", "c", "d", "e"]


if __name__ == "__main__":
    unittest.main()