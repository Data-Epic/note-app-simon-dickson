from datetime import datetime

class Note:
    #The Base class for notes
    note_counter = 0  # Class variable to generate unique IDs

    def __init__(self, content: str):
        #This initializes a note with content and timestamp.
        self.id = Note.note_counter + 1
        Note.note_counter += 1
        self.content = content
        self.created_at = datetime.now()

    def display(self):
        # This displays note details (can be overridden by subclasses).
        return f"[{self.id}] {self.created_at.strftime('%Y-%m-%d %H:%M:%S')} - {self.content}"
