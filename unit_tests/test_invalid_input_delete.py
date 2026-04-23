import unittest
from unittest.mock import patch
import main 


class TestInvalidInputDelete(unittest.TestCase):

    def setUp(self):
        main.tasks.clear()
        main.tasks.append({
            "title": "Test task", 
            "completed": False,
            "deadline": None
        })
    
    @patch("main.safe_input", return_value="")
    def test_delete_task_empty_input(self, mock_input):
        main.delete_tasks()
        self.assertEqual(len(main.tasks), 1)

    @patch("main.safe_input", return_value="abc")
    def test_delete_task_non_numeric_input(self, mock_input):
        main.delete_tasks()
        self.assertEqual(len(main.tasks), 1)

    @patch("main.safe_input", return_value="999")
    def test_delete_task_out_of_range_input(self, mock_input):
        main.delete_tasks()
        self.assertEqual(len(main.tasks), 1)

    @patch("main.safe_input", return_value=None)
    def test_delete_task_none_input(self, mock_input):
        main.delete_tasks()
        self.assertEqual(len(main.tasks), 1)

    @patch("main.safe_input", return_value="0")
    def test_delete_task_zero_input(self, mock_input):
        main.delete_tasks()
        self.assertEqual(len(main.tasks), 1)
    
    @patch("main.safe_input", return_value="-1")
    def test_delete_task_negative_input(self, mock_input):
        main.delete_tasks()
        self.assertEqual(len(main.tasks), 1)

    @patch("main.safe_input", return_value="1")
    def test_delete_task_valid_input(self, mock_input):
        main.delete_tasks()
        self.assertEqual(len(main.tasks), 0)
    
    @patch("main.safe_input", return_value="2")
    def test_delete_removes_correct_task(self, mock_input):
        main.tasks.clear()
        main.tasks.append({
            "title": "Task 1",
            "completed": False,
            "deadline": None
        })
        main.tasks.append({
            "title": "Task 2", 
            "completed": False,
            "deadline": None
        })

        main.delete_tasks()

        self.assertEqual(len(main.tasks), 1)
        self.assertEqual(main.tasks[0]["title"], "Task 1")

    def test_delete_no_tasks(self):
        main.tasks.clear()
        main.delete_tasks()
        self.assertEqual(main.tasks,[])
