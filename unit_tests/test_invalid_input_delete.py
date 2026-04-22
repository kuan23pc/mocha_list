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
    def test_delete_task_empty_input_does_not_crash(self, mock_input):
        try:
            main.delete_tasks()
        except Exception as e:
            self.fail(f"delete_tasks crashed on empty input: {e}")
        self.assertEqual(len(main.tasks), 1)

    @patch("main.safe_input", return_value="abc")
    def test_delete_task_non_numeric_input_does_not_crash(self, mock_input):
        try:
            main.delete_tasks()
        except Exception as e:
            self.fail(f"delete_tasks crashed on non-numeric input: {e}")
        self.assertEqual(len(main.tasks), 1)

    @patch("main.safe_input", return_value="999")
    def test_delete_task_out_of_range_input_does_not_crash(self, mock_input):
        try:
            main.delete_tasks()
        except Exception as e:
            self.fail(f"delete_tasks crashed on out-of-range input: {e}")
        self.assertEqual(len(main.tasks), 1)

    @patch ("main.safe_input", return_value=None)
    def test_delete_task_keyboard_interrupt_does_not_crash(self, mock_input):
        try:
            main.delete_tasks()
        except Exception as e:
            self.fail(f"delete_tasks crashed on KeyboardInterrupt: {e}")
        self.assertEqual(len(main.tasks), 1)
    
    @patch ("main.safe_input", return_value="0")
    def test_delete_task_zero_input_does_not_crash(self, mock_input):
        try:
            main.delete_tasks()
        except Exception as e:
            self.fail(f"delete_tasks crashed on zero input: {e}")
        self.assertEqual(len(main.tasks), 1)

    @patch("main.safe_input", return_value="-1")
    def test_delete_task_negative_input_does_not_crash(self, mock_input):
        try:
            main.delete_tasks()
        except Exception as e:
            self.fail(f"delete_tasks crashed on negative input: {e}")
        self.assertEqual(len(main.tasks), 1)

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

        self.assertEqual(len(main.tasks),1)
        self.assertEqual(main.tasks[0]["title"], "Task 1")

if __name__ == "__main__":
    unittest.main()