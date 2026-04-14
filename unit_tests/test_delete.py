import unittest    #pythons built-in unit testing framework
from unittest.mock import patch #patch så we can fake inputs 
import main


class TestDeleteTasks(unittest.TestCase):

    def setUp(self): 
        self.original_tasks = main.tasks.copy()  #save the original tasks to restore later

    def tearDown(self):  #runs after every test to clean up
        main.tasks.clear()   #remove any tasks added during tests
        main.tasks.extend(self.original_tasks)  #put back the original

    @patch("main.save_tasks")  #fake save_tasks to the test so it does not write to jonsson
    @patch("builtins.print")   #fake print so we can check what is printed without actually printing to the console
    @patch("main.safe_input", return_value="1")
    def test_delete_existing_task(self, mock_input, mock_print, mock_save):
        main.tasks.clear()
        main.tasks.extend([  #add fake tasks for the test 
            {"title": "Task 1", "completed": False, "deadline": None},
            {"title": "Task 2", "completed": False, "deadline": None}
        ])

        main.delete_tasks() #run the delete function

        self.assertEqual(len(main.tasks), 1)
        self.assertEqual(main.tasks[0]["title"], "Task 2")
        mock_print.assert_any_call("Task 'Task 1' deleted!")

    @patch("builtins.print")
    def test_delete_when_no_tasks_exist(self, mock_print):
        main.tasks.clear()

        main.delete_tasks()

        mock_print.assert_any_call("No tasks available to delete.")

    @patch("builtins.print")
    @patch("main.safe_input", return_value="abc")
    def test_delete_with_invalid_input(self, mock_input, mock_print):
        main.tasks.clear()
        main.tasks.extend([
            {"title": "Task 1", "completed": False, "deadline": None}
        ])

        main.delete_tasks()

        self.assertEqual(len(main.tasks), 1)
        mock_print.assert_any_call("Please enter a valid number.")

    @patch("builtins.print")
    @patch("main.safe_input", return_value="5")
    def test_delete_with_non_existing_task_number(self, mock_input, mock_print):
        main.tasks.clear()
        main.tasks.extend([
            {"title": "Task 1", "completed": False, "deadline": None}
        ])

        main.delete_tasks()

        self.assertEqual(len(main.tasks), 1)
        mock_print.assert_any_call("Task number not found.")

    @patch("builtins.print")
    @patch("main.safe_input", return_value="")
    def test_delete_with_empty_input(self, mock_input, mock_print):
        main.tasks.clear()
        main.tasks.extend([
            {"title": "Task 1", "completed": False, "deadline": None}
        ])

        main.delete_tasks()

        self.assertEqual(len(main.tasks), 1)
        mock_print.assert_any_call("Task number cannot be empty.")


if __name__ == "__main__":
    unittest.main()