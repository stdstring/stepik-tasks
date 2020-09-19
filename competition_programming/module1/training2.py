import typing
import unittest


def generate(n: int) -> typing.List[typing.List[int]]:
    def generate_impl(used_numbers_mask: int, current_seq: typing.List[int], dest: typing.List[typing.List[int]]) -> None:
        for number in range(1, n + 1):
            if (used_numbers_mask & (1 << number)) == 0:
                if len(current_seq) == (n - 1):
                    dest.append(current_seq + [number])
                    return
                else:
                    generate_impl(used_numbers_mask | (1 << number), current_seq + [number], dest)
    permutations = []
    generate_impl(0, [], permutations)
    return permutations


class TestTaskImplementation(unittest.TestCase):

    def test_task(self):
        n = 7
        lex_number = 4468
        self.assertEqual([7, 2, 3, 1, 5, 6, 4], generate(n)[lex_number - 1])


if __name__ == "__main__":
    unittest.main()