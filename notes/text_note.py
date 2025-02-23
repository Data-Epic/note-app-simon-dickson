from .base import Note

class TextNote(Note):
    """A simple text-based note"""

    def display(self):
        """Displays a text note"""
        return f"Text Note {super().display()}"
