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


class TestLoadTasks(unittest.TestCase):
    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file.close()

        self.original_file = main.FILE_NAME
        self.original_tasks = copy.deepcopy(main.tasks)

        main.FILE_NAME = self.temp_file.name

    def tearDown(self):
        main.FILE_NAME = self.original_file
        main.tasks.clear()
        main.tasks.extend(self.original_tasks)

        if os.path.exists(self.temp_file.name):
            os.remove(self.temp_file.name)

    def test_load_tasks_reads_valid_data(self):
        sample_tasks = [
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

        with open(self.temp_file.name, "w") as file:
            json.dump(sample_tasks, file)

        loaded_tasks = main.load_tasks()

        self.assertEqual(loaded_tasks, sample_tasks)

    def test_load_tasks_returns_empty_list_when_file_missing(self):
        os.remove(self.temp_file.name)

        loaded_tasks = main.load_tasks()

        self.assertEqual(loaded_tasks, [])

    @patch("builtins.print")
    def test_load_tasks_returns_empty_list_for_invalid_json(self, mock_print):
        with open(self.temp_file.name, "w") as file:
            file.write("{ invalid json")

        loaded_tasks = main.load_tasks()

        self.assertEqual(loaded_tasks, [])
        mock_print.assert_called_with("Invalid JSON file. Starting with an empty list.")

    @patch("builtins.print")
    def test_load_tasks_returns_empty_list_for_invalid_format(self, mock_print):
        invalid_data = {
            "title": "This should be a list, not a dictionary"
        }

        with open(self.temp_file.name, "w") as file:
            json.dump(invalid_data, file)

        loaded_tasks = main.load_tasks()

        self.assertEqual(loaded_tasks, [])
        mock_print.assert_called_with("Invalid task file format. Starting with an empty list.")

    @patch("builtins.print")
    def test_load_tasks_handles_file_read_error(self, mock_print):
        with patch("builtins.open", side_effect=OSError("Permission denied")):
            loaded_tasks = main.load_tasks()

        self.assertEqual(loaded_tasks, [])
        mock_print.assert_called_with("Error reading file: Permission denied")


if __name__ == "__main__":
    unittest.main()
