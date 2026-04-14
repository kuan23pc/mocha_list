import unittest
import main
import builtins

class TestAddTask(unittest.TestCase):

    def setUp(self):
        self.original_input = main.safe_input
        self.original_save = main.save_tasks
        self.original_print = builtins.print

        main.tasks = [] #Reset tasks before each test

        #Replace input with fixed value
        main.safe_input = lambda _: "Test task"

        #Disable file writing
        main.save_tasks = lambda: None

        #Disable print output
        builtins.print = lambda *args, **kwargs: None

    def tearDown(self):
        #Restore original functions
        main.safe_input = self.original_input
        main.save_tasks = self.original_save
        builtins.print = self.original_print

    def test_add_valid_task(self):
        #simulate user input
        main.safe_input = lambda _: "Test task"

        #Run function
        main.add_task()

        #Check that one task was added
        self.assertEqual(len(main.tasks), 1)

        #Check content
        self.assertEqual(main.tasks[0]["title"], "Test task")
        self.assertFalse(main.tasks[0]["completed"])
        self.assertIsNone(main.tasks[0]["deadline"])

    def test_add_empty_task(self):
        #simulate empty input
        main.safe_input = lambda _: ""

        main.add_task()

        #no task should be added
        self.assertEqual(len(main.tasks), 0)

    def test_add_none_input(self):
        #simulate cancelled input
        main.safe_input = lambda _: None

        main.add_task()

        #No task should be added
        self.assertEqual(len(main.tasks), 0)

if __name__ == "__main__":
    unittest.main()