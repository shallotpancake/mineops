import unittest
from minecraft import install
from curseforge.helpers import get_mod_id, get_latest_server_file_url
import const
from pathlib import Path
from main import main
import sys

class TestMainFunction(unittest.TestCase):
    def test_main_runs_successfully(self):
        # Call the main function and check its result
        print("=========test_main_runs_successfully=========")
        result = main()
        self.assertEqual(result, 0)

class TestCurseforgeCredential(unittest.TestCase):
    
    def setUp(self):
        self.cred_path = const.CURSEFORGE_SECRET_PATH

    def test_credential_file_exists(self):
        print("=========test_credential_file_exists=========")
        result = Path.is_file(self.cred_path)
        self.assertTrue(result)

    def test_curseforge_credential(self):
        print("=========test_curseforge_credential=========")
        result = get_mod_id(1)
        self.assertIsNotNone(result)

class TestServerInstall(unittest.TestCase):
    def test_server_directory_size(self):
        print("=========test_server_directory_size=========")
        # check number of subdirectories
        # should be 0 or 1
        # most packs extract into a release folder i.e. Server-Files-2.20
        subdirectories = len([item for item in const.SERVER_DIR.iterdir() if item.is_dir()])
        self.assertNotEqual(subdirectories, 1)

class TestCurseforgeHelpers(unittest.TestCase):
    def test_get_latest_files(self):
        print("=========test_get_latest_files=========")
        result = get_latest_server_file_url(mod_id=925200)
        self.assertIsNotNone(result)


if __name__ == "__main__":
    # Redirect stdout to a file for the entire script
    TEST_LOG_FILE_PATH = const.TEST_LOG_FILE_PATH
    with open(TEST_LOG_FILE_PATH, "w", encoding='utf8') as log_file:
        sys.stdout = log_file  # Redirect all print statements to the log file
        try:
            unittest.main()  # Run the tests
        finally:
            sys.stdout = sys.__stdout__  # Restore stdout
            print(f"Test output:\n  {TEST_LOG_FILE_PATH}")
