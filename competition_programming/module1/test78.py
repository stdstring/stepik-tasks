import typing
import unittest


bracket_map = {"(": ")", "[": "]"}


def generate(n: int) -> typing.List[str]:
    def generate_impl(bracket_stack: typing.List[str], current_sequence: str, dest: typing.List[str]) -> typing.List[str]:
        if (2 * n - len(bracket_stack)) == len(current_sequence):
            dest.append(current_sequence + "".join(bracket_stack[::-1]))
            return dest
        for bracket in ["(", ")", "[", "]"]:
            if (bracket == "(") or (bracket == "["):
                dest = generate_impl(bracket_stack + [bracket_map[bracket]], current_sequence + bracket, dest)
            if (bracket == ")") or (bracket == "]"):
                if (len(bracket_stack) != 0 ) and (bracket_stack[-1] == bracket):
                    dest = generate_impl(bracket_stack[:-1], current_sequence + bracket, dest)
        return dest
    return generate_impl([], "", [])


class TestTaskImplementation(unittest.TestCase):

    def test_example(self):
        n = 2
        lex_number = 6
        self.assertEqual("[[]]", generate(n)[lex_number - 1])

    def test_task1(self):
        n = 3
        lex_number = 20
        self.assertEqual("([][])", generate(n)[lex_number - 1])

    def test_task2(self):
        n = 7
        lex_number = 8233
        self.assertEqual("(([]())([]))()", generate(n)[lex_number - 1])


if __name__ == "__main__":
    unittest.main()
