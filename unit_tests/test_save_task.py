import copy
import importlib.util
import json
import os
import tempfile
import unittest
from unittest.mock import patch

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
MAIN_PATH = os.path.join(PROJECT_ROOT, "main.py")

spec = importlib.util.spec_from_file_location("task_app_under_test", MAIN_PATH)
main = importlib.util.module_from_spec(spec)
spec.loader.exec_module(main)


class TestSaveTasks(unittest.TestCase):
    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file.close()

        self.sample_tasks = [
            {
                "title": "Test Task 1",
                "completed": False,
                "deadline": None
            },
            {
                "title": "Test Task 2",
                "completed": True,
                "deadline": "2026-04-20"
            }
        ]

        self.original_file = main.FILE_NAME
        self.original_tasks = copy.deepcopy(main.tasks)

        main.FILE_NAME = self.temp_file.name
        main.tasks.clear()
        main.tasks.extend(copy.deepcopy(self.sample_tasks))

    def tearDown(self):
        main.FILE_NAME = self.original_file
        main.tasks.clear()
        main.tasks.extend(self.original_tasks)

        if os.path.exists(self.temp_file.name):
            os.remove(self.temp_file.name)

    def test_save_tasks_writes_correct_data(self):
        main.save_tasks()

        with open(self.temp_file.name, "r") as file:
            data = json.load(file)

        self.assertEqual(data, self.sample_tasks)

    def test_save_tasks_creates_valid_json(self):
        main.save_tasks()

        with open(self.temp_file.name, "r") as file:
            data = json.load(file)

        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]["title"], "Test Task 1")

    @patch("builtins.print")
    def test_save_tasks_handles_file_error(self, mock_print):
        with patch("builtins.open", side_effect=OSError("Permission denied")):
            main.save_tasks()

        mock_print.assert_called_with("Error saving file: Permission denied")


if __name__ == "__main__":
    unittest.main()