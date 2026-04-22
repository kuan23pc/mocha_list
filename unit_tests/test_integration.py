import unittest
import json
import os
import main

# Integration tests for full workflows in the task manager
class TestIntegration(unittest.TestCase):
    # Setup before each test: reset tasks and use a tempory file
    def setUp(self):
        main.tasks.clear()
        self.test_file = "test_tasks.json"
        self.original_file_name = main.FILE_NAME
        main.FILE_NAME = self.test_file

    # Cleanup after each test: remove temp file and restore filename
    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        main.FILE_NAME = self.original_file_name
    
    # Test 1: add, save, file exists
    def test_add_task(self):
        main.safe_input = lambda _: "Task A"

        main.add_task()
        #Check file was created
        self.assertTrue(os.path.exists(self.test_file))

        # Verify saved content
        with open(self.test_file) as f: 
            data = json.load(f)

        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["title"], "Task A")

    # Test 2, add, complete, saved in file
    def test_complete_task(self): 
        main.safe_input = lambda _: "Task B"
        main.add_task()

        # Select first task
        main.safe_input = lambda _: "1"
        main.mark_task_completed()

        # Verify completion status in file
        with open(self.test_file) as f:
            data = json.load(f)

        self.assertTrue(data[0]["completed"])

    # Test 3: add, delete, file updated

    def test_delete_task(self):
        main.safe_input = lambda _: "Task C"
        main.add_task()

        main.safe_input = lambda _: "1"
        main.delete_tasks()

        with open(self.test_file) as f:
            data = json.load(f)

        self.assertEqual(len(data), 0)


    # Test 4: add, set deadline, saved
    def test_set_deadline(self):
        main.safe_input = lambda _: "Task D"
        main.add_task()

        inputs = iter(["1", "2099-12-31"])
        main.safe_input = lambda _: next(inputs)

        main.set_deadline()

        with open(self.test_file) as f:
            data = json.load(f)

        self.assertEqual(data[0]["deadline"], "2099-12-31")

    # Test 5: Invalid delete input
    def test_invalid_input(self): 
        main.safe_input = lambda _: "Task X"
        main.add_task()

        main.safe_input = lambda _: "abc"
        main.delete_tasks()

        with open(self.test_file) as f:
            data = json.load(f)
        
        self.assertEqual(len(data), 1)

    # Test 6: invalid deadline format
    def test_invalid_deadline(self):
        main.safe_input = lambda _: "Task Y"
        main.add_task()

        inputs = iter(["1", "invalid-date"])
        main.safe_input = lambda _: next(inputs)

        main.set_deadline()

        with open(self.test_file) as f:
            data = json.load(f)
        
        self.assertIsNone(data[0]["deadline"])

    # Test 7: empty complete input
    def test_empty_complete(self):
        main.safe_input = lambda _: "Task E"
        main.add_task()

        main.safe_input = lambda _: ""
        main.mark_task_completed()

        with open(self.test_file) as f:
            data = json.load(f)

        self.assertFalse(data[0]["completed"])

    # Test 8: Empty add task
    def test_add_empty(self):
        main.safe_input = lambda _: ""
        main.add_task()

        self.assertEqual(len(main.tasks), 0)

    # Test 9: None input add task  
    def test_add_none(self):
        main.safe_input = lambda _: None
        main.add_task()

        self.assertEqual(len(main.tasks), 0)
    
    
if __name__ == "__main__":
    unittest.main()