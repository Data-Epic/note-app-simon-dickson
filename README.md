# note-app-simon-dickson

This is a simple command-line application for creating, deleting, displaying, and searching notes. The application supports both **text notes** and **reminder notes** with scheduled reminder times.

## Features

- Add text-based notes
- Add reminder notes with a specified date and time
- Delete notes by ID
- View all stored notes
- Search for notes based on keywords

## Project Structure

## File Breakdown

### `base_note.py`
Defines the **Note** class, a base class for all types of notes. It handles ID assignment, note content, and timestamps.

### `text_note.py`
Implements the **TextNote** class, inheriting from `Note`. It provides a formatted display method for text notes.

### `reminder_note.py`
Implements the **ReminderNote** class, inheriting from `Note`. It adds an extra attribute for storing the reminder time and validates the time format.

### `manager.py`
Handles the core **notes management** functionalities:
- Adding new text or reminder notes
- Deleting notes by ID
- Listing all stored notes
- Searching notes by keywords

### `main.py`
The entry point of the application. Provides an **interactive CLI** for users to manage notes.

---

## Prerequisites

Ensure you have Python **3.7 or later** installed.

### Install Dependencies
No external libraries are required, as the project only uses Python’s built-in modules.

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

### Error Handling
- Reminder notes must follow the format YYYY-MM-DD HH:MM AM/PM, otherwise an error is raised.
- If an invalid note type is entered, an error message is displayed.
- If a user tries to delete a non-existent note ID, an appropriate message is shown.