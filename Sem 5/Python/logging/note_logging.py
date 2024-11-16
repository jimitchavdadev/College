import logging
import os

# Define the path where the log file should be saved
log_directory = '/home/rebel/Roger/College/Sem 5/Python/logging'
log_file = 'notes.log'
log_path = os.path.join(log_directory, log_file)

# Ensure the directory exists, or create it
os.makedirs(log_directory, exist_ok=True)

# Configure logging to log messages to the specified directory and file
logging.basicConfig(filename=log_path, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def add_note(note):
    """
    Function to add a note to the log and return confirmation.
    """
    logging.info(f'Adding note: {note}')
    return f'Note added: {note}'

def delete_note(note):
    """
    Function to delete a note from the log and return confirmation.
    """
    logging.info(f'Deleting note: {note}')
    return f'Note deleted: {note}'

def list_notes(notes):
    """
    Function to lista    all notes. Returns a string of notes or a message if no notes exist.
    """
    logging.info('Listing all notes.')
    return "\n".join(notes) if notes else "No notes available."

def check_input(note):
    """
    Function to validate the note input. 
    Ensures the note is a non-empty string. Logs an error if validation fails.
    """
    if not isinstance(note, str) or len(note.strip()) == 0:
        logging.error("Invalid Input: Note cannot be empty or non-string.")
        return False
    return True

def main():
    """
    Main function to manage the note-taking system. 
    Provides options to add, delete, list notes, or exit the system.
    """
    notes = []  # List to store notes
    
    while True:
        # User selects an action
        action = input("Choose an action (add, delete, list, exit): ").strip().lower()
        
        if action == 'add':
            # Adding a new note
            note = input("Enter the note to add: ")
            if check_input(note):
                result = add_note(note)  # Log and confirm the added note
                notes.append(note)  # Append to the notes list
                print(result)
            else:
                print("Invalid input. Please enter a valid note.")

        elif action == 'delete':
            # Deleting an existing note
            note = input("Enter the note to delete: ")
            if note in notes:
                result = delete_note(note)  # Log and confirm the deleted note
                notes.remove(note)  # Remove from the notes list
                print(result)
            else:
                # Error handling if note is not found
                logging.warning(f"Attempted to delete a non-existing note: {note}")
                print("Note not found.")

        elif action == 'list':
            # Listing all notes
            result = list_notes(notes)
            print(result)

        elif action == 'exit':
            # Exit the note management system
            logging.info('Exiting the note management system.')
            print("Exiting the note management system.")
            break

        else:
            # Error handling for invalid action
            logging.error(f"Invalid action: No Action Selected")
            print("Invalid action. Please choose from add, delete, list, or exit.")

if __name__ == '__main__':
    main()
