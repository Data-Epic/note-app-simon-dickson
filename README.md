# note-app-simon-dickson

This is a simple command-line application for creating, deleting, displaying, and searching notes. The application supports both **text notes** and **reminder notes** with scheduled reminder times.

## Features

- Add text-based notes
- Add reminder notes with a specified date and time
- Delete notes by ID
- View all stored notes
- Search for notes based on keywords
- Comprehensive **unit testing** with `pytest`

## Project Structure

### File Breakdown

#### `base_note.py`
Defines the **Note** class, a base class for all types of notes. It handles ID assignment, note content, and timestamps.

#### `text_note.py`
Implements the **TextNote** class, inheriting from `Note`. It provides a formatted display method for text notes.

#### `reminder_note.py`
Implements the **ReminderNote** class, inheriting from `Note`. It adds an extra attribute for storing the reminder time and validates the time format.

#### `manager.py`
Handles the core **notes management** functionalities:
- Adding new text or reminder notes
- Deleting notes by ID
- Listing all stored notes
- Searching notes by keywords

#### `main.py`
The entry point of the application. Provides an **interactive CLI** for users to manage notes.

#### `tests/`
Contains unit tests for the application, written with **pytest** to ensure reliability.

---

## Prerequisites

Ensure you have Python **3.7 or later** installed.

### Install Dependencies
No external libraries are required, as the project only uses Python’s built-in modules.

To install `pytest` for testing, run:
```bash
pip install pytest
```

---

## Cloning the Project

To get started, clone the repository:

```bash
git clone https://github.com/Data-Epic/note-app-simon-dickson.git
```
---
## Running the script

In the root directory, run the script:
```bash
python main.py
```

## Usage
Once the script is running, you’ll see an interactive prompt with available commands:
```bash
Options: add, delete, show, search, exit
Enter command:
```

## Adding Notes

### Text Note:
```bash
Enter note type (text/reminder): text
Enter note content: Buy groceries
```

### Reminder Note:
```bash
Enter note type (text/reminder): reminder
Enter note content: Doctor’s appointment
Enter reminder time (YYYY-MM-DD HH:MM AM/PM): 2025-02-22 10:30 AM
```

## Deleting Notes
```bash
Enter note ID to delete: 1
```

## Viewing Notes

### If no notes exist:
```bash
No notes available.
```
### Otherwise:
```bash
Text Note [1] 2025-02-21 18:45:00 - Buy groceries
```

## Searching Notes
```bash
Enter keyword to search: groceries
```
## Error Handling
- Reminder notes must follow the format YYYY-MM-DD HH:MM AM/PM, otherwise an error is raised.
- If an invalid note type is entered, an error message is displayed.
- If a user tries to delete a non-existent note ID, an appropriate message is shown.

---

## Running Tests with Pytest

This project includes unit tests to validate its functionality. To run the tests, execute:
```bash
pytest tests/test_notes_manager.py
```

### Understanding Pytest Usage in This Project

The testing suite ensures the correctness of various operations, including adding, deleting, and searching notes. Here are some core pytest concepts used:

#### `assert`
- Used to validate test conditions.
- Example:
  ```python
  assert len(found_notes) == 2  # Ensures the expected number of search results
  ```

#### `len()`
- A built-in function used to determine the number of elements in a sequence.
- Example:
  ```python
  notes = ["Note 1", "Note 2"]
  assert len(notes) == 2  # Passes if the length is 2
  ```

#### `isinstance()`
- Ensures that an object belongs to a specific class.
- Example:
  ```python
  assert isinstance(note, TextNote)  # Checks if 'note' is an instance of TextNote
  ```

#### `capsys`
- A pytest fixture that captures `stdout` and `stderr` output during a test.
- Example:
  ```python
  def test_display_notes(capsys):
      notes_manager.display_notes()
      captured = capsys.readouterr()
      assert "No notes available." in captured.out  # Verifies printed output
  ```

#### `captured`
- A variable storing the output captured by `capsys.readouterr()`.
- Example:
  ```python
  captured = capsys.readouterr()
  print(captured.out)  # Displays the captured output
  ```

### Example Test Case
```python
import pytest
from manager import NotesManager

def test_search_notes():
    notes_manager = NotesManager()
    notes_manager.add_note("text", "Programming is not fun")
    notes_manager.add_note("text", "It keeps me on my seat for lots of hours")
    notes_manager.add_note("text", "Pytest makes programming easier")
    
    found_notes = notes_manager.search_notes("programming")
    assert len(found_notes) == 2 # Two notes should contain 'programming'
```

---

---