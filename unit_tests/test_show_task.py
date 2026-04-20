import unittest
import main
import builtins
from io import StringIO
import sys
from datetime import datetime, timedelta

class TestShowTasks(unittest.TestCase):

    def setUp(self):
        #Save original stdout
        self.original_stdout = sys.stdout

        #Reset tasks before each test
        main.tasks = []

        # Capture printed output
        self.captured_output = StringIO()
        sys.stdout = self.captured_output

    def tearDown(self):
        #Restore stdout
        sys.stdout = self.original_stdout

    def test_show_tasks_with_data(self):
        # Create a future deadline dynamically
        future_date = (datetime.today() + timedelta(days=10)).strftime("%Y-%m-%d")

        # Set test data
        main.tasks = [
            {"title": "Test task 1", "completed": False, "deadline": None},
            {"title": "Test task 2", "completed": True, "deadline": future_date}
        ]

        #Run fun. 
        main.show_tasks()

        # Get output
        output = self.captured_output.getvalue()

        # Assertions
        self.assertIn("Task List", output)
        self.assertIn("Test task 1", output)
        self.assertIn("Test task 2", output)

        self.assertIn("Completed", output)
        self.assertIn(future_date, output)  # extra check

    def test_show_tasks_empty(self):
        #Ensure tasks list is empty
        main.tasks = []

        #Run function
        main.show_tasks()

        #Get output
        output = self.captured_output.getvalue()

        #Assertion
        self.assertIn("No tasks available", output)


if __name__ == "__main__":
    unittest.main()
