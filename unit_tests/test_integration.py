import unittest
import json
import os
import main

class TestIntegration(unittest.TestCase):
    def setUp(self):
        main.tasks.clear()
        self.test_file = "test_tasks.json"
        self.original_file_name = main.FILE_NAME
        main.FILE_NAME = self.test_file

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        main.FILE_NAME = self.original_file_name
    
    #Test 1: add, save, file exists
    def test_add_task(self):
        main.safe_input = lambda _: "Task A"

        main.add_task()

        self.assertTrue(os.path.exists(self.test_file))

        with open(self.test_file) as f: 
            data = json.load(f)

        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["title"], "Task A")

    #Test 2, add, complete, saved in file
    def test_complete_task(self): 
        main.safe_input = lambda _: "Task B"
        main.add_task()

        main.safe_input = lambda _: "1"
        main.mark_task_completed()

        with open(self.test_file) as f:
            data = json.load(f)

        self.assertTrue(data[0]["completed"])

    #Test 3: add, delete, file updated

    def test_delete_task(self):
        main.safe_input = lambda _: "Task C"
        main.add_task()

        main.safe_input = lambda _: "1"
        main.delete_tasks()

        with open(self.test_file) as f:
            data = json.load(f)

        self.assertEqual(len(data), 0)


    #Test 4: add, set deadline, saved
    def test_set_deadline(self):
        main.safe_input = lambda _: "Task D"
        main.add_task()

        inputs = iter(["1", "2099-12-31"])
        main.safe_input = lambda _: next(inputs)

        main.set_deadline()

        with open(self.test_file) as f:
            data = json.load(f)

        self.assertEqual(data[0]["deadline"], "2099-12-31")

     # Test 5: save and load tasks
    def test_save_and_load_tasks_integration(self):
        main.tasks.clear()
        main.tasks.append({
            "title": "Integration Task",
            "completed": False,
            "deadline": None
        })

        main.save_tasks()

        main.tasks.clear()
        loaded_tasks = main.load_tasks()

        self.assertEqual(len(loaded_tasks), 1)
        self.assertEqual(loaded_tasks[0]["title"], "Integration Task")
        self.assertFalse(loaded_tasks[0]["completed"])
        self.assertIsNone(loaded_tasks[0]["deadline"])



if __name__ == "__main__":
    unittest.main()