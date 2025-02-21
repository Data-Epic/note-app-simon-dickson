from manager import NotesManager

def main():
    """Interactive command-line interface for managing notes."""
    notes_manager = NotesManager()
    
    while True:
        print("\nOptions: add, delete, show, search, exit")
        choice = input("Enter command: ").strip().lower()

        if choice == "add":
            note_type = input("Enter note type (text/reminder): ").strip().lower()
            content = input("Enter note content: ").strip()
            reminder_time = None
            if note_type == "reminder":
                reminder_time = input("Enter reminder time (YYYY-MM-DD HH:MM AM/PM): ").strip()
            try:
                notes_manager.add_note(note_type, content, reminder_time)
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "delete":
            try:
                note_id = int(input("Enter note ID to delete: "))
                notes_manager.delete_note(note_id)
            except ValueError:
                print("Invalid ID. Please enter a number.")

        elif choice == "show":
            notes_manager.show_notes()

        elif choice == "search":
            keyword = input("Enter keyword to search: ").strip()
            notes_manager.search_notes(keyword)

        elif choice == "exit":
            print("Exiting program.")
            break

        else:
            print("Invalid command. Try again.")

if __name__ == "__main__":
    main()
