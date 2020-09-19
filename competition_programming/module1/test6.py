import unittest


def check_bracket_sequence(sequence: str) -> bool:
    bracket_stack = []
    for bracket in sequence:
        if bracket == "(":
            bracket_stack.append(")")
        if bracket == "[":
            bracket_stack.append("]")
        if (bracket == ")") or (bracket == "]"):
            if (len(bracket_stack) == 0) or (bracket_stack.pop() != bracket):
                return False
    return len(bracket_stack) == 0


class TestTaskImplementation(unittest.TestCase):

    def test_task(self):
        self.assertEqual(True, check_bracket_sequence("()()[[[]()]]([()][][()[]])[]()()"))
        self.assertEqual(False, check_bracket_sequence("[[]](()()[[[]]][]()()()[()])()]"))
        self.assertEqual(False, check_bracket_sequence("[[[((]))[](][)(()())]][[][]()[]]"))
        self.assertEqual(False, check_bracket_sequence("(()[([][]())[()][()][][])]([])()"))
        self.assertEqual(True, check_bracket_sequence("(()[([][]())[()][()][][]])([])()"))


if __name__ == "__main__":
    unittest.main()