import os
import sys

# Define custom exceptions for error handling
class FileNotFoundError(Exception):
    def __init__(self, message="The specified file was not found."):
        self.message = message
        super().__init__(self.message)  # Call the base class constructor

class InvalidInputDataError(Exception):
    def __init__(self, message="The input data is invalid."):
        self.message = message
        super().__init__(self.message)  # Call the base class constructor

class DiskSpaceFullError(Exception):
    def __init__(self, message="Not enough disk space to write the output file."):
        self.message = message
        super().__init__(self.message)  # Call the base class constructor

# Simulate disk space limit (1 MB)
DISK_SPACE_LIMIT_MB = 1  # Set disk space limit in megabytes
DISK_SPACE_LIMIT_BYTES = DISK_SPACE_LIMIT_MB *1024*1024 # Convert limit to bytes

def read_input_file(file_path):
    # Check if the specified file exists
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File '{file_path}' not found.")  # Raise custom exception if file is not found
    with open(file_path, 'r') as file:  # Open the file for reading
        return file.read()  # Return the content of the file

def process_text_data(text):
    # Check if the input data is a string
    if not isinstance(text, str):
        raise InvalidInputDataError("Input data must be a string.")  # Raise custom exception for invalid input
    word_count = len(text.split())  # Count the number of words in the text
    char_freq = {}  # Initialize a dictionary to store character frequencies
    for char in text:  # Iterate through each character in the text
        char_freq[char] = char_freq.get(char, 0) + 1  # Count occurrences of each character
    return word_count, char_freq  # Return the word count and character frequency dictionary

def write_output_file(file_path, data):
    # Check if the output file size exceeds the disk space limit
    if os.path.getsize(file_path) > DISK_SPACE_LIMIT_BYTES:
        raise DiskSpaceFullError("Not enough disk space to write the output file.")  # Raise custom exception if space is insufficient
    with open(file_path, 'w') as file:  # Open the file for writing
        file.write(data)  # Write the processed data to the file

def main():
    try:
        # Define input and output file paths
        input_file = '/home/rebel/Roger/College/Sem 5/Python/04_09_2024/input.txt'  # Replace with actual input file path
        output_file = '/home/rebel/Roger/College/Sem 5/Python/04_09_2024/output.txt'  # Replace with actual output file path
        
        # Step 1: Read the input file
        text = read_input_file(input_file)
        
        # Step 2: Process the text data
        word_count, char_freq = process_text_data(text)  # Get word count and character frequencies
        processed_data = f"Word Count: {word_count}\nCharacter Frequencies:\n{char_freq}"  # Format the processed data
        
        # Step 3: Write the output file
        write_output_file(output_file, processed_data)  # Write the processed data to the output file
        print("Processing complete. Results written to output file.")  # Print completion message
    
    except FileNotFoundError as e:
        print(e)  # Print error message for file not found
    except InvalidInputDataError as e:
        print(e)  # Print error message for invalid input data
    except DiskSpaceFullError as e:
        print(e)  # Print error message for insufficient disk space
    except Exception as e:
        print(f"An unexpected error occurred: {e}")  # Print any other unexpected errors

if __name__ == "__main__":
    main()  # Execute the main function