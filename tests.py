import unittest
from main import main

class TestMainFunction(unittest.TestCase):
    def test_main_runs_successfully(self):
        # Call the main function and check its result
        result = main()
        self.assertEqual(result, 0)

if __name__ == "__main__":
    unittest.main()
