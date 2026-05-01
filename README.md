# CALM List

[![CI](https://github.com/kuan23pc/group_project/actions/workflows/ci.yml/badge.svg)](https://github.com/kuan23pc/group_project/actions)
 

## Project Description 
CALM List is a desktop task management application built with Python. 

It helps users organize their daily tasks, manage deadlines, track progress, and improve productivity. 

The application supports both a **Command Line Interface (CLI)** and a **Graphical User Interface (GUI)**. 

## Team Members

| Name | GitHub Username |
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

### Task Management
- Add new tasks
- Edit existing tasks
- Delete tasks
- Mark tasks as completed
- Clear completed tasks
- Add task descriptions
- Set and update deadlines

### Organization
- Create multiple task lists
- Rename lists
- Delete lists
- Navigate between lists through the sidebar 

### Productivity
- Filter tasks: All, Active, Completed
- View total, completed, and remaining tasks
- Progress bar showing completion percentage

### Interfaces
- Command Line Interface (CLI) 
- Graphical User Interface (GUI)

### Data Storage
- Save tasks automatically to file 
- Load tasks when starting the application


## How It Works
The application can be used in two different ways: 

### Command Line Interface (CLI)
Users interact with the program through terminal commands. 

### Graphical User Interface (GUI)
Users manage tasks visually through a Tkinter desktop interface. 

Both interfaces use the same stored data, allowing users to switch between CLI and GUI. 


## Programming Language
The project is implemented in Python 3. 

Python is used because it provides the necessary functionality for handling user input, data structures, and file operations in a console-based application. 

The program follows a modular structure with separate functions for different responsibilities. 


## Build System 
No external build system is required.

The application is executed using the Python interpreter and does not depend on external libraries.


## How to Run the Project
The program is a task manager that can be run as both a CLI and GUI application. 

To run the program, follow these steps: 
1. Open a terminal
2. Clone the repository:
    
    ```bash
   git clone https://github.com/kuan23pc/calm_list.git
   ```
3. Navigate to the project folder by writing: 
     
     ```bash
     cd CALM_List
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


## Workflow 
- Each feature will be developed in a separate branch
- Pull requests will be used before merging into main
- Code reviews will be done by team members
- No direct commits to the main branch 
 

## How to Run the Unit Tests
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

## How to Run a Linter
To check code quality, install flake8: 

```bash
python -m pip install flake8
```

Run the linter: 

```bash
python -m flake8 .
```

This will analyze the code and display any style or formatting issues.
