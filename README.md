# group_project
Group project for software engineering course 

## Project description 
This project aims to develop a task mangagement system that enables users to create, organize, and track tasks. The system is desgined to help users manage their daily activties and improve productivity. In addition, it alows users to keep track of deadlines in a structured way.

## Team members

| Name | GitHub username |
|------|------------------|
| Andjela Kuzmanovski | @kuan23pc |
| Isabella Laazar |@issaabellaa |
| Christina Outra |@christinaoutra |
| Marina Alramo |@marinaalr |

## Declarations 

I, Andjela Kuzamanovski, Declare that I am the sole author of the content that I add to this repository. 

I, Marina Alramo, Declare that I am the sole author of the content that I add to this repository.

I, Isabella Lazar, declare that I am the sole author of the content I add to this repository.

I, Christina Outra, declare that I am the sole author of the content I add to this repository.
   

## Planed features 
- Add new tasks
- Delete existing tasks
- Mark tasks as completed
- Set and update deadlines
- Sort tasks by deadline or priority
- Assign priority levels using color indicators
- View all tasks in a list
- Save tasks in a file
- Load tasks from a file

## How it will work 
The application will run as a command line interface. Users can interact with the system by typing commands to add, remove, or update tasks. Each task can include a title, a deadline, and a priority level. In addition, tasks will be saved to a file so they remain available after the program is closed. When the program starts, it will load the previously saved tasks from the file. The system will provide feedback after each command. 

## Programming Language
The project will be implemented in Python 3. 

Python is used because it provides the necessary functionality for handling user input, data structures, and file operations in a console-based application. 

The program will be structured using object-oriented programming principles. 

## Build System 
No external build system is required.

The application is executed using the Python interpreter and does not depend on any external libraries.

## How to Run the Project
The program is a console-based task manager written in Python. 

To run the program, follow these steps: 
  1. Open a terminal
  2. Clone the repository:
    
     git clone https://github.com/kuan23pc/group_project.git
  3. Navigate to the project folder by writing: 
     
     cd group_project
  4. Run the program by writing: 
     
     python main.py

## Kanban Board 
You can find our Kanban Board here: https://github.com/users/kuan23pc/projects/1

## Work flow 
- Each feature will be developed in a separate branch
- Pull requests will be used before merging into main
- Code reviews will be done by team members
- No direct commits to the main branch 
 
 ## How to run the unit tests
To run all unit tests, make sure you are in the root directory of the project. 

Run the following command in the terminal: 

python -m unittest discover


This command will automatically find and execute all unit tests in the project.

The tests verify different functionalities of the system, including task creation, completion, and handling of invalid input. 

## Coverage
To generate code coverage, install coverage: 

python -m pip install coverage


un the tests with coverage: 

python -m coverage run -m unittest discover -s unit_tests


Then generate a report: 

python -m coverage report

## How to run a linter
To check code quality, install flake8: 

python -m pip install flake8

Run the linter: 

python -m flake8 .

This will analyze the code and display any style or formatting issues.