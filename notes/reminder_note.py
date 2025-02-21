from datetime import datetime
from .base import Note

class ReminderNote(Note):
    """A note with an additional reminder date and time"""

    def __init__(self, content: str, reminder_time: str):
        """Initialize a reminder note with content and a reminder time."""
        super().__init__(content)
        try:
            self.reminder_time = datetime.strptime(reminder_time, "%Y-%m-%d %I:%M %p")
        except ValueError:
            raise ValueError("Reminder time must be in format: YYYY-MM-DD HH:MM AM/PM")

    def display(self):
        """Displays a reminder note"""
        return f"Reminder Note {super().display()} | Reminder: {self.reminder_time.strftime('%Y-%m-%d %I:%M %p')}"
