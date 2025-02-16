import csv

# Function to calculate the average grade from a list of grades
def calculate_average(grades):
    if len(grades) == 0:
        return 0
    return sum(grades) / len(grades)

# Function to load student data from a CSV file and calculate average grades
def load_and_process_student_data(filename):
    student_averages = {}  
    
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            student_name = row['Name']  
            
            grades = []
            for i in range(1, 6):
                subject_key = f'Subject {i}'
                # converting each subject grade to float and handle errors if the value is invalid
                try:
                    if subject_key in row and row[subject_key].strip():
                        grade = float(row[subject_key])
                        grades.append(grade)
                except ValueError as e:
                    print(f"Warning: Invalid grade '{row[subject_key]}' for {student_name} in {subject_key}. Error: {e}")
            
            average_grade = calculate_average(grades)
            
            student_averages[student_name] = average_grade
            
    return student_averages  

# Function to write the student averages to a new CSV file
def write_averages_to_csv(averages, output_filename):
    with open(output_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        writer.writerow(['Name', 'Average'])
        
        for student, average in averages.items():
            writer.writerow([student, average])

# Define the input and output file names
input_filename = '/home/rebel/Roger/College/Sem 5/Python/14_08_2024/student_grades.csv'  
output_filename = 'student_average_grades.csv'  

# Load student data, calculate averages, and write the results to a new CSV file
student_averages = load_and_process_student_data(input_filename)  
write_averages_to_csv(student_averages, output_filename)  
