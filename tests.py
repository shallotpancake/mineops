import unittest
from minecraft import install_server
from curseforge.helpers import get_mod_id
from const import CURSEFORGE_SECRET_PATH
from pathlib import Path
from main import main

class TestMainFunction(unittest.TestCase):
    def test_main_runs_successfully(self):
        # Call the main function and check its result
        result = main()
        self.assertEqual(result, 0)

class TestCurseforgeCredential(unittest.TestCase):
    
    def setUp(self):
        self.cred_path = CURSEFORGE_SECRET_PATH

    def test_credential_file_exists(self):
        result = Path.is_file(self.cred_path)
        self.assertTrue(result)

    def test_curseforge_credential(self):
        result = get_mod_id(1)
        self.assertIsNotNone(result)

if __name__ == "__main__":
    unittest.main()
