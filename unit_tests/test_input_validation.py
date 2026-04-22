import unittest
from unittest.mock import patch
import main


class TestInputValidation(unittest.TestCase):

    def setUp(self):
        main.tasks.clear()

    # 🔥 Test main loop (exit direkt)
    def test_main_exit(self):
        with patch("builtins.input", side_effect=["6"]):
            main.main()

    # 🔥 Test invalid input i main
    def test_main_invalid_then_exit(self):
        with patch("builtins.input", side_effect=["99", "6"]):
            main.main()

    # 🔥 safe_input exception (KeyboardInterrupt)
    def test_safe_input_interrupt(self):
        with patch("builtins.input", side_effect=KeyboardInterrupt):
            result = main.safe_input("Test")

        self.assertIsNone(result)

    # 🔥 delete: None input
    def test_delete_none_input(self):
        main.tasks.append({"title": "Test", "completed": False, "deadline": None})

        with patch("main.safe_input", return_value=None):
            main.delete_tasks()

        self.assertEqual(len(main.tasks), 1)

    # 🔥 delete: empty input
    def test_delete_empty_input(self):
        main.tasks.append({"title": "Test", "completed": False, "deadline": None})

        with patch("main.safe_input", return_value=""):
            main.delete_tasks()

        self.assertEqual(len(main.tasks), 1)

    # 🔥 delete: negativt index
    def test_delete_negative_index(self):
        main.tasks.append({"title": "Test", "completed": False, "deadline": None})

        with patch("main.safe_input", return_value="-1"):
            main.delete_tasks()

        self.assertEqual(len(main.tasks), 1)

    # 🔥 deadline i dåtid
    def test_deadline_in_past(self):
        main.tasks.append({"title": "Test", "completed": False, "deadline": None})

        with patch("main.safe_input", side_effect=["1", "2000-01-01"]):
            main.set_deadline()

        self.assertIsNone(main.tasks[0]["deadline"])


if __name__ == "__main__":
    unittest.main()