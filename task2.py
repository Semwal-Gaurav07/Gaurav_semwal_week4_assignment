import csv

def calculate_student_averages(input_file, output_file):
    try:
        # Dictionary to store each student's average grade
        student_averages = {}

        # Open and read the CSV file
        with open(input_file, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                student_name = row["Student"]
                grades = [float(row[subject]) for subject in row if subject != "Student" and row[subject]]
                
                if grades:  # Ensure there are grades to calculate
                    average_grade = sum(grades) / len(grades)
                    student_averages[student_name] = average_grade
                else:
                    student_averages[student_name] = None  # No grades available

        # Write the averages to the output file
        with open(output_file, mode='w', encoding='utf-8') as output_csv:
            writer = csv.writer(output_csv)
            writer.writerow(["Student", "Average Grade"])
            for student, average in student_averages.items():
                writer.writerow([student, f"{average:.2f}" if average is not None else "N/A"])

        print(f"Averages calculated and saved to '{output_file}'")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except ValueError:
        print("Error: Non-numeric value found in the grade columns.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Specify the input and output file paths
input_file = 'student_grades.csv'
output_file = 'student_averages.csv'

# Run the function
calculate_student_averages(input_file, output_file)


