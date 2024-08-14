import csv

# Function to calculate the average grade from a list of grades
def calculate_average(grades):
    # Check if the list is empty to avoid division by zero
    if len(grades) == 0:
        return 0
    # Calculate and return the average grade
    return sum(grades) / len(grades)

# Function to load student data from a CSV file and calculate average grades
def load_and_process_student_data(filename):
    student_averages = {}  # Dictionary to store student names and their average grades
    
    # Open the CSV file for reading
    with open(filename, mode='r') as file:
        # Create a CSV reader object to read the file
        reader = csv.DictReader(file)
        
        # Iterate over each row in the CSV file
        for row in reader:
            student_name = row['Name']  # Extract the student's name
            
            # Extract grades for the five subjects from the row
            grades = [float(row[f'Subject {i}']) for i in range(1, 6) if f'Subject {i}' in row]
            
            # Calculate the average grade for the student
            average_grade = calculate_average(grades)
            
            # Store the student's name and average grade in the dictionary
            student_averages[student_name] = average_grade
            
    return student_averages  # Return the dictionary of student averages

# Function to write the student averages to a new CSV file
def write_averages_to_csv(averages, output_filename):
    # Open the output CSV file for writing
    with open(output_filename, mode='w', newline='') as file:
        # Create a CSV writer object to write data to the file
        writer = csv.writer(file)
        
        # Write the header row with column names
        writer.writerow(['Name', 'Average'])
        
        # Iterate over the student averages dictionary
        for student, average in averages.items():
            # Write each student's name and average grade to the file
            writer.writerow([student, average])

# Define the input and output file names
input_filename = 'student_grades.csv'  # Input CSV file with student grades
output_filename = 'student_average_grades.csv'  # Output CSV file with average grades

# Load student data, calculate averages, and write the results to a new CSV file
student_averages = load_and_process_student_data(input_filename)  # Load data and calculate averages
write_averages_to_csv(student_averages, output_filename)  # Write the averages to the output CSV file
