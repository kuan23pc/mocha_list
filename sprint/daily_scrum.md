# Daily Scrum Log

## Day 1
- Marina: Started planning improvements for display format and how to connect deadlines to tasks.
- Christina: Started working on delete using index
- Andjela: Started working on input validation improvements
- Isabella: Started working on persisting completed status in JSON.


Next steps:
- Begin implementing core functionality


Blockers:
- Marina: Needed to decide how the display format should be structured for clarity.
- Christina: Uncertainty about handling invalid indices in delete functionality.
- Andjela: Needed to define validation rules for different types of input.
- Isabella: Needed to determine how to structure JSON data for persistence.


## Day 2
- Marina: Worked on improving display format and delete functionality using index.
- Christina: Worked together with Marina on delete using index and helped finalize the functionality.
- Andjela: Continued working on input validation improvements.
- Isabella: Continued working on persisting completed status in JSON.


Next steps:
- Continue implementing remaining features
- Start connecting deadlines to tasks


Blockers:
- Marina: Minor issues with Git when merging changes
- Christina: Needed to handle edge cases for delete functionality.
- Andjela: Handling different types of invalid user input.
- Isabella: Issues with saving and loading data consistently.


## Day 3
- Marina: Completed the display frmat improvements and tested the functionality.
- Christina: Completed the delete using index functionality.
- Andjela: Continued working on input validation improvements.
- Isabella: Continued finalizing her code for persisting completed status in JSON, faced some complications with the system.


Next steps:
- Finalize remaining implementations
- Create PR for completed features
- Prepare for code review and merge approved changes into main
- Test all features together.


Blockers
- Marina: Ensuring constistent output formatting across all features.
- Christina: Verifying behavior for edge cases in delete functionality.
- Andjela: Finalizing validation rules for all input scenarios.
- Isabella: Some complications related to system integration and data handling.

## day 4 
Isabella: implemented saving of completed task status. task are now stored in JSON with both title and complation staus, so progress is not lost when the program restarts. So the issue i done

Marina: Improvd how tasks are displayed to make the output clearer and easier to read. Formatting was updated so tasks and their status are shown in a more strutured and user-frindly way. 
Christina: Done with the issue, improved the deadine fetures by adding input validation, program now only accepts dates in the format yyy-mm-dd and rejects invalid or past dates. Updated the mark completed features to use task index insted of title. All issue done.
Andjela: Improved input validation in the program, program now handles invalid user input more safely and prevents crashes by checking values before processing them
Blockers:
isabella- some problem with joson file
Chrisitina- forgot to put in a svae function in issue so all changes diespered when exit
Marina- Fix bug in json file
Andjela- 
