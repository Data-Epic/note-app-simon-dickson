from typing import List
from notes.text_note import TextNote
from notes.reminder_note import ReminderNote
from notes.base import Note

class NotesManager:
    """Manages a collection of notes"""

    def __init__(self):
        """Initialize an empty list to store notes."""
        self.notes: List[Note] = []

    def add_note(self, note_type: str, content: str, reminder_time: str = None):
        """Creates and adds a note of the specified type."""
        if note_type.lower() == "text":
            note = TextNote(content)
        elif note_type.lower() == "reminder":
            if reminder_time is None:
                raise ValueError("Reminder time is required for ReminderNote")
            note = ReminderNote(content, reminder_time)
        else:
            raise ValueError("Invalid note type. Use 'text' or 'reminder'.")
        self.notes.append(note)
        print(f"Note added: {note.display()}")

    def delete_note(self, note_id: int):
        """Removes a note by ID."""
        self.notes = [note for note in self.notes if note.id != note_id]
        print(f"Deleted note with ID {note_id}")

    def show_notes(self):
        """Displays all stored notes."""
        if not self.notes:
            print("No notes available.")
        else:
            for note in self.notes:
                print(note.display())

    def search_notes(self, keyword: str):
        """Finds notes that contain a specific keyword."""
        found_notes = [note for note in self.notes if keyword.lower() in note.content.lower()]
        if not found_notes:
            print(f"No notes found with keyword: {keyword}")
        else:
            for note in found_notes:
                print(note.display())
