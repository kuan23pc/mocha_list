import main


def test_completed_persistence(tmp_path):
    test_file = tmp_path / "tasks.json"

    old_file_name = main.FILE_NAME
    old_tasks = list(main.tasks)

    try:
        main.FILE_NAME = str(test_file)
        main.tasks.clear()

        main.tasks.append({
            "title": "Test task",
            "completed": False,
            "deadline": None
        })

        main.tasks[0]["completed"] = True

        main.save_tasks()

        main.tasks.clear()

        loaded = main.load_tasks()

        assert len(loaded) == 1
        assert loaded[0]["title"] == "Test task"
        assert loaded[0]["completed"] is True
        assert loaded[0]["deadline"] is None

    finally:
        main.FILE_NAME = old_file_name
        main.tasks.clear()
        main.tasks.extend(old_tasks)


def test_load_invalid_json(tmp_path):
    test_file = tmp_path / "tasks.json"
    test_file.write_text("{ invalid json }", encoding="utf-8")

    old_file_name = main.FILE_NAME

    try:
        main.FILE_NAME = str(test_file)

        loaded = main.load_tasks()

        assert loaded == []

    finally:
        main.FILE_NAME = old_file_name