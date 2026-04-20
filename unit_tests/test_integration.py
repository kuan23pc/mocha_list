import unittest
import json
import os
import main

class TestIntegration(unittest.TestCase):
    def setUp(self):
        main.tasks.clear()
        self.test_file = "test_tasks.json"
        main.FILE_NAME = self.test_file

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
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

    #Test 4: add, set deadline, saved


if __name__ == "__main__":
    unittest.main()