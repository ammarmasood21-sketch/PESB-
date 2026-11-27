# Beginner To-Do List Manager

A beginner-level command-line To-Do List project based on the uploaded
"Project To-Do List Manager" presentation.

## Run the project

1. Extract the ZIP file.
2. Open the `Beginner_ToDo_List_Manager` folder in VS Code.
3. Open the terminal.
4. Run:

   `python todo.py`

## Menu options

1. Add a task
2. View all tasks
3. Mark a task as done
4. Delete a task
5. Exit with a done/pending summary

## Python concepts used

- Variables and strings
- `input()` and `print()`
- Lists and dictionaries
- List indexing
- `append()` and `pop()`
- `len()`
- `if`, `elif`, and `else`
- `while` and `for` loops
- `break`
- Comparison operators
- f-strings

The project follows the core requirements in the presentation. The optional
bonus features (edit, undo, search, and saving tasks to a file) are not included.
The program stores tasks in memory, so tasks are cleared when the program exits.

## Example task structure

Each task is stored as a dictionary:

`{"title": "Buy groceries", "done": False}`

All task dictionaries are kept in the `tasks` list.
