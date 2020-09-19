import unittest


def check_sequence(sequence: str) -> bool:
    balance_value = 0
    for bracket in sequence:
        if bracket == "(":
            balance_value += 1
        if bracket == ")":
            if balance_value == 0:
                return False
            else:
                balance_value -= 1
    return balance_value == 0


class TestTaskImplementation(unittest.TestCase):

    def test_task(self):
        self.assertEqual(True, check_sequence("(())(())()"))
        self.assertEqual(True, check_sequence("(()())(())"))
        self.assertEqual(False, check_sequence("((((())))"))
        self.assertEqual(False, check_sequence("((())())))"))
        self.assertEqual(False, check_sequence("(()))((())"))


if __name__ == "__main__":
    unittest.main()