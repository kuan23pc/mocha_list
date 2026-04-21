# Mocha List

[![CI](https://github.com/kuan23pc/group_project/actions/workflows/ci.yml/badge.svg)](https://github.com/kuan23pc/group_project/actions)
 

## Project description 
Mocha List is a task management system that allows users to create, organize, and track tasks. The system is designed to help users manage their daily activities and improve productivity. 

The application supports deadlines and provides a structured way to manage tasks.

## Team members

| Name | GitHub username |
|------|------------------|
| Andjela Kuzamanovski | @kuan23pc |
| Isabella Lazar | @issaabellaa |
| Christina Outra | @christinaoutra |
| Marina Alramo | @marinaalr |

## Declarations 

I, Andjela Kuzamanovski, declare that I am the sole author of the content that I add to this repository. 

I, Marina Alramo, declare that I am the sole author of the content that I add to this repository.

I, Isabella Lazar, declare that I am the sole author of the content I add to this repository.

I, Christina Outra, declare that I am the sole author of the content I add to this repository.
   

## Features 
- Add new tasks
- Delete existing tasks
- Mark tasks as completed
- Set and update deadlines
- Add descriptions to tasks
- Filter tasks (all, active, completed)
- View all tasks in a list
- Save tasks in a file
- Load tasks from a file
- GUI interface for visual task management. 

## How it will work 
The application can be used in two different ways: 

### Command Line Interface (CLI)
Users interact with the system by typing commands in the terminal. 

### Graphical User Interface (GUI)
Users can manage tasks visually using a Tkinter-based interface. 

Both interfaces use the same data stored in a JSON file. 

## Programming Language
The project is implemented in Python 3. 

Python is used because it provides the necessary functionality for handling user input, data structures, and file operations in a console-based application. 

The program follows a modular structure with seperate functions for different responsibilities. 

## Build System 
No external build system is required.

The application is executed using the Python interpreter and does not depend on external libraries.

## How to Run the Project
The program is a task manager that can be run as both a CLI and GUI application. 

To run the program, follow these steps: 
1. Open a terminal
2. Clone the repository:
    
    ```bash
   git clone https://github.com/kuan23pc/mocha_list.git
   ```
3. Navigate to the project folder by writing: 
     
     ```bash
     cd mocha_list
     ```
4. Run the program by writing: 
     
     ### CLI
     ```bash
     python main.py
     ```

     ### GUI
      ```bash
     python gui.py
     ```

## Kanban Board 
You can find our Kanban Board here: [Kanban Board](https://github.com/users/kuan23pc/projects/1)

## Work flow 
- Each feature will be developed in a separate branch
- Pull requests will be used before merging into main
- Code reviews will be done by team members
- No direct commits to the main branch 
 
 ## How to run the unit tests
To run all unit tests, make sure you are in the root directory of the project. 

Run the following command in the terminal: 

```bash
python -m unittest discover -s unit_tests
```

This command will automatically find and execute all unit tests in the project.

The tests verify different functionalities of the system, including task creation, completion, and handling of invalid input. 

## Code Coverage
To generate code coverage, install coverage: 

```bash
python -m pip install coverage
```

Run the tests with coverage:

```bash
python -m coverage run -m unittest discover -s unit_tests
```

Then generate a report: 

```bash
python -m coverage report
```

## How to run a linter
To check code quality, install flake8: 

```bash
python -m pip install flake8
```

Run the linter: 

```bash
python -m flake8 .
```

This will analyze the code and display any style or formatting issues.
