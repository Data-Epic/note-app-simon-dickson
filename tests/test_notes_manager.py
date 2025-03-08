import pytest
from manager import NotesManager
from notes.text_note import TextNote
from notes.reminder_note import ReminderNote

@pytest.fixture
def notes_manager():
    return NotesManager()

def test_add_text_note(notes_manager):
    notes_manager.add_note("text", "A test note")
    assert len(notes_manager.notes) == 1
    assert isinstance(notes_manager.notes[0], TextNote)
    assert notes_manager.notes[0].content == "A test note"

def test_add_reminder_note(notes_manager):
    notes_manager.add_note("reminder", "30 minutes to your date", "2025-02-14 07:00 PM")
    assert len(notes_manager.notes) == 1
    assert isinstance(notes_manager.notes[0], ReminderNote)
    assert notes_manager.notes[0].content == "30 minutes to your date"

def test_add_reminder_note_without_time(notes_manager):
    with pytest.raises(ValueError, match="Reminder time is required for ReminderNote"):
        notes_manager.add_note("reminder", "No time specified")

def test_delete_note(notes_manager):
    notes_manager.add_note("text", "Delete this note")
    note_id = notes_manager.notes[0].id
    notes_manager.delete_note(note_id)
    assert len(notes_manager.notes) == 0

def test_search_notes(notes_manager):
    notes_manager.add_note("text", "Programming is not fun")
    notes_manager.add_note("text", "It keeps me on my seat for lots of hours")
    notes_manager.add_note("text", "Pytest makes programming easier")
    
    found_notes = notes_manager.search_notes("programming")
    assert len(found_notes) == 2

def test_show_notes(capsys, notes_manager):
    notes_manager.add_note("text", "My first note")
    notes_manager.add_note("text", "My second note")
    
    notes_manager.show_notes()
    captured = capsys.readouterr()
    assert "My first note" in captured.out
    assert "My second note" in captured.out
