import typing
import unittest


def generate(n: int) -> typing.List[str]:
    def generate_impl(current_balance: int, current_sequence:int, dest: typing.List[str]) -> None:
        if (current_balance + len(current_sequence)) == (2 * n) :
            dest.append(current_sequence + current_balance * ")")
            return
        if current_balance == 0:
            generate_impl(1, current_sequence + "(", dest)
        else:
            for bracket in ["(", ")"]:
                generate_impl(current_balance + (1 if bracket == "(" else -1), current_sequence + bracket, dest)
    brackets = []
    generate_impl(0, "", brackets)
    return brackets


class TestTaskImplementation(unittest.TestCase):

    def test_task(self):
        n = 10
        lex_number = 8644
        self.assertEqual("(()(()()))()()()(())", generate(n)[lex_number - 1])


if __name__ == "__main__":
    unittest.main()