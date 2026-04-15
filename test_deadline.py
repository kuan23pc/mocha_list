from datetime import date, timedelta
import main


def test_set_deadline(monkeypatch):
    main.tasks.clear()
    main.tasks.append({
        "title": "Test task", 
        "completed": False,
        "deadline": None

    })

    future_date = (date.today() + timedelta(days=7)).strftime("%Y-%m-%d")

    inputs = iter(["1", future_date])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main.set_deadline()

    assert main.tasks[0]["deadline"] == future_date