import os

# Custom Exception Classes
class FileNotFoundError(Exception):
    def __init__(self, message="The specified input file was not found."):
        self.message = message
        super().__init__(self.message)

class InvalidInputDataError(Exception):
    def __init__(self, message="The input data is invalid."):
        self.message = message
        super().__init__(self.message)

class DiskSpaceFullError(Exception):
    def __init__(self, message="There is not enough disk space to write the output file."):
        self.message = message
        super().__init__(self.message)

# Text Processing Tool
class TextProcessor:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def read_input(self):
        if not os.path.isfile(self.input_file):
            raise FileNotFoundError(f"Input file '{self.input_file}' not found.")
        
        with open(self.input_file, 'r') as file:
            data = file.read()
        
        if not isinstance(data, str):
            raise InvalidInputDataError("The input data is not a string or is missing.")
        
        return data

    def process_data(self, data):
        if not isinstance(data, str):
            raise InvalidInputDataError("The input data is not a valid string.")
        
        word_count = len(data.split())
        char_freq = {char: data.count(char) for char in set(data)}
        
        return word_count, char_freq

    def write_output(self, word_count, char_freq):
        try:
            with open(self.output_file, 'w') as file:
                file.write(f"Word Count: {word_count}\n")
                file.write("Character Frequencies:\n")
                for char, freq in char_freq.items():
                    file.write(f"{char}: {freq}\n")
        except OSError as e:
            if e.errno == 28:  # No space left on device
                raise DiskSpaceFullError()
            else:
                raise

    def run(self):
        try:
            data = self.read_input()
            word_count, char_freq = self.process_data(data)
            self.write_output(word_count, char_freq)
            print("Processing completed successfully.")
        except (FileNotFoundError, InvalidInputDataError, DiskSpaceFullError) as e:
            print(f"Error: {e}")

# Example Usage
if __name__ == "__main__":
    input_file = '/home/rebel/Roger/College/Sem 5/Python/04_09_2024/input.txt'  # Path to the input file
    output_file = '/home/rebel/Roger/College/Sem 5/Python/04_09_2024/output.txt'  # Path to the output file

    processor = TextProcessor(input_file, output_file)
    processor.run()
