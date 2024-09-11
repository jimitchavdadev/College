import os
import sys

# Define custom exceptions
class FileNotFoundError(Exception):
    def __init__(self, message="The specified file was not found."):
        self.message = message
        super().__init__(self.message)

class InvalidInputDataError(Exception):
    def __init__(self, message="The input data is invalid."):
        self.message = message
        super().__init__(self.message)

class DiskSpaceFullError(Exception):
    def __init__(self, message="Not enough disk space to write the output file."):
        self.message = message
        super().__init__(self.message)

# Simulate disk space limit (1 MB)
DISK_SPACE_LIMIT_MB = 1
DISK_SPACE_LIMIT_BYTES = DISK_SPACE_LIMIT_MB * 1024 * 1024

def read_input_file(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File '{file_path}' not found.")
    with open(file_path, 'r') as file:
        return file.read()

def process_text_data(text):
    if not isinstance(text, str):
        raise InvalidInputDataError("Input data must be a string.")
    word_count = len(text.split())
    char_freq = {}
    for char in text:
        char_freq[char] = char_freq.get(char, 0) + 1
    return word_count, char_freq

def write_output_file(file_path, data):
    if os.path.getsize(file_path) > DISK_SPACE_LIMIT_BYTES:
        raise DiskSpaceFullError("Not enough disk space to write the output file.")
    with open(file_path, 'w') as file:
        file.write(data)

def main():
    try:
        input_file = '/home/rebel/Roger/College/Sem 5/Python/04_09_2024/input.txt'  # Replace with actual input file path
        output_file = '/home/rebel/Roger/College/Sem 5/Python/04_09_2024/output.txt'  # Replace with actual output file path
        
        # Step 1: Read the input file
        text = read_input_file(input_file)
        
        # Step 2: Process the text data
        word_count, char_freq = process_text_data(text)
        processed_data = f"Word Count: {word_count}\nCharacter Frequencies:\n{char_freq}"
        
        # Step 3: Write the output file
        write_output_file(output_file, processed_data)
        print("Processing complete. Results written to output file.")
    
    except FileNotFoundError as e:
        print(e)
    except InvalidInputDataError as e:
        print(e)
    except DiskSpaceFullError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
