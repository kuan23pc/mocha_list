import main

def test_add_task(monkeypatch):
    #Replace input() so it returns a fixed value for testing
    monkeypatch.setattr("builtins.input", lambda _: "Test task")

    #Disable saving to file to avoid modifying tasks.json
    monkeypatch.setattr(main, "save_tasks", lambda: None)

    # Reset the global tasks list before running the test
    main.tasks = []

    #Call the fun. we want to test
    main.add_task()

    #Verify that one task is added
    assert len(main.tasks) == 1

    #Verify the task content
    assert main.tasks[0]["title"] == "Test task"
    assert main.tasks[0]["completed"] is False
    assert main.tasks[0]["deadline"] is None