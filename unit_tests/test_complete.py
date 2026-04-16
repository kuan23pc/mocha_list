import unittest
from unittest.mock import patch
import main


class TestMarkTaskCompleted(unittest.TestCase):

    def setUp(self):
        self.original_tasks = main.tasks.copy()  #save original tasks before each test

    def tearDown(self):
        main.tasks.clear()
        main.tasks.extend(self.original_tasks)  #restore tasks after each test

    @patch("main.save_tasks")  #avoid writing to the real JSON file
    @patch("builtins.print")   #let us check printed messages
    @patch("main.safe_input", return_value="1")  #fake user input
    def test_mark_existing_task_completed(self, mock_input, mock_print, mock_save):
        main.tasks.clear()
        main.tasks.extend([
            {"title": "Task 1", "completed": False, "deadline": None},
            {"title": "Task 2", "completed": False, "deadline": None}
        ])

        main.mark_task_completed()

        self.assertTrue(main.tasks[0]["completed"])
        self.assertFalse(main.tasks[1]["completed"])
        mock_print.assert_any_call("Task 'Task 1' marked as completed!")

    @patch("builtins.print")
    def test_mark_task_when_no_tasks_exist(self, mock_print):
        main.tasks.clear()

        main.mark_task_completed()

        mock_print.assert_any_call("No tasks available.")

    @patch("builtins.print")
    @patch("main.safe_input", return_value="abc")  #invalid input
    def test_mark_task_with_invalid_input(self, mock_input, mock_print):
        main.tasks.clear()
        main.tasks.extend([
            {"title": "Task 1", "completed": False, "deadline": None}
        ])

        main.mark_task_completed()

        self.assertFalse(main.tasks[0]["completed"])
        mock_print.assert_any_call("Please enter a valid number.")

    @patch("builtins.print")
    @patch("main.safe_input", return_value="5")  #number does not exist
    def test_mark_task_with_non_existing_task_number(self, mock_input, mock_print):
        main.tasks.clear()
        main.tasks.extend([
            {"title": "Task 1", "completed": False, "deadline": None}
        ])

        main.mark_task_completed()

        self.assertFalse(main.tasks[0]["completed"])
        mock_print.assert_any_call("Task number not found.")

    @patch("builtins.print")
    @patch("main.safe_input", return_value="")  #empty input
    def test_mark_task_with_empty_input(self, mock_input, mock_print):
        main.tasks.clear()
        main.tasks.extend([
            {"title": "Task 1", "completed": False, "deadline": None}
        ])

        main.mark_task_completed()

        self.assertFalse(main.tasks[0]["completed"])
        mock_print.assert_any_call("Task number cannot be empty.")


if __name__ == "__main__":
    unittest.main()