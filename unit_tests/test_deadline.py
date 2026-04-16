import unittest
from unittest.mock import patch
from datetime import date, timedelta
import main


class TestSetDeadline(unittest.TestCase):

    @patch("builtins.input")
    def test_set_deadline(self, mock_input):
        main.tasks.clear()
        main.tasks.append({
            "title": "Test task",
            "completed": False,
            "deadline": None
        })

        future_date = (date.today() + timedelta(days=7)).strftime("%Y-%m-%d")

        mock_input.side_effect = ["1", future_date]

        main.set_deadline()

        self.assertEqual(main.tasks[0]["deadline"], future_date)

if __name__ == "__main__":
    unittest.main()
