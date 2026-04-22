import unittest
from unittest.mock import patch
from datetime import date, timedelta
import main


class TestSetDeadline(unittest.TestCase):

    def setUp(self):
        main.tasks.clear()

    @patch("builtins.input")
    def test_set_deadline(self, mock_input):

        main.tasks.append({
            "title": "Test task",
            "completed": False,
            "deadline": None
        })

        future_date = (date.today() + timedelta(days=7)).strftime("%Y-%m-%d")
        mock_input.side_effect = ["1", future_date]

        main.set_deadline()

        self.assertEqual(main.tasks[0]["deadline"], future_date)

    @patch("builtins.input", return_value="")
    def test_set_deadline_empty_task_number(self,mock_input):
        main.tasks.append({
            "title": "Test task", 
            "completed": False,
            "deadline": None
        })
        main.set_deadline()
        self.assertIsNone(main.tasks[0]["deadline"])
    
    @patch("builtins.input", return_value="abc")
    def test_setdeadline_invalid_task_number(self, mock_input):
        main.tasks.append({
            "title": "Test task",
            "completed": False,
            "deadline": None

        })

        main.set_deadline()
        self.assertIsNone(main.tasks[0]["deadline"])
    
    @patch("builtins.input", return_value="999")
    def test_set_deadline_out_of_range_task_number(self, mock_input):
        main.tasks.append({
            "title": "Test task",
            "completed": False,
            "deadline": None
        })
        
        main.set_deadline()

        self.assertIsNone(main.tasks[0]["deadline"])

    @patch("builtins.input", side_effect=["1", ""])
    def test_set_deadline_empty_deadline(self, mock_input):
        main.tasks.append({
            "title": "Test task",
            "completed": False,
            "deadline": None
        })

        main.set_deadline()

        self.assertIsNone(main.tasks[0]["deadline"])

    @patch("builtins.input", side_effect=["1", "2025/01/01"])
    def test_set_deadline_invalid_date_format(self, mock_input):
        main.tasks.append({
            "title": "Test task",
            "completed": False,
            "deadline": None
        })

        main.set_deadline()
        
        self.assertIsNone(main.tasks[0]["deadline"])
    
    def test_set_deadline_no_tasks(self):
        main.set_deadline()
        self.assertEqual(main.tasks, [])

    @patch("builtins.input", side_effect=["1", "2000-01-01"])
    def test_set_deadine_past_date(self, mock_input):
        main.tasks.append({
            "title": "Test task",
            "completed": False,
            "deadline": None
        })
        
        main.set_deadline()

        self.assertIsNone(main.tasks[0]["deadline"])

        


if __name__ == "__main__":
    unittest.main()
