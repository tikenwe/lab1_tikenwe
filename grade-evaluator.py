import csv
import sys
import os

def load_csv_data():
    """
    Prompts the user for a filename, checks if it exists, 
    and extracts all fields into a list of dictionaries.
    """
    filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ")

    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)

    assignments = []

    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })
        return assignments
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)


def evaluate_grades(data):
    """
    Implement your logic here.
    'data' is a list of dictionaries containing the assignment records.
    """
    print("\n--- Processing Grades ---")

    if not data:
        print("Error: No assignment records found. The CSV file appears to be empty.")
        return

    invalid_scores = [row for row in data if row['score'] < 0 or row['score'] > 100]
    if invalid_scores:
        print("Error: The following assignments have scores outside the 0-100 range:")
        for row in invalid_scores:
            print(f"  - {row['assignment']}: {row['score']}")
        return

    formative_rows = [row for row in data if row['group'].strip().lower() == 'formative']
    summative_rows = [row for row in data if row['group'].strip().lower() == 'summative']

    total_weight = sum(row['weight'] for row in data)
    formative_weight = sum(row['weight'] for row in formative_rows)
    summative_weight = sum(row['weight'] for row in summative_rows)

    if round(total_weight, 2) != 100:
        print(f"Error: Total weight must equal 100. Found {total_weight}.")
        return
    if round(formative_weight, 2) != 60:
        print(f"Error: Formative weights must sum to 60. Found {formative_weight}.")
        return
    if round(summative_weight, 2) != 40:
        print(f"Error: Summative weights must sum to 40. Found {summative_weight}.")
        return

    total_grade = sum(row['score'] * row['weight'] / 100 for row in data)
    gpa = (total_grade / 100) * 5.0

    formative_points = sum(row['score'] * row['weight'] / 100 for row in formative_rows)
    summative_points = sum(row['score'] * row['weight'] / 100 for row in summative_rows)

    formative_pct = (formative_points / formative_weight) * 100 if formative_weight else 0
    summative_pct = (summative_points / summative_weight) * 100 if summative_weight else 0

    status = "PASSED" if formative_pct >= 50 and summative_pct >= 50 else "FAILED"

    failed_formatives = [row for row in formative_rows if row['score'] < 50]
    resubmission_list = []

    if failed_formatives:
        highest_weight = max(row['weight'] for row in failed_formatives)
        resubmission_list = [row for row in failed_formatives if row['weight'] == highest_weight]

    print(f"Formative Score: {formative_pct:.2f}%  (weight pool: {formative_weight})")
    print(f"Summative Score: {summative_pct:.2f}%  (weight pool: {summative_weight})")
    print(f"Total Grade: {total_grade:.2f}/100")
    print(f"Final GPA: {gpa:.2f}/5.0")
    print(f"Final Status: {status}")

    if resubmission_list:
        print("\nResubmission Eligible (failed formative assignment(s) with the highest weight):")
        for row in resubmission_list:
            print(f"  - {row['assignment']} (Score: {row['score']}, Weight: {row['weight']})")
    else:
        print("\nNo formative assignments are eligible for resubmission.")


if __name__ == "__main__":
    course_data = load_csv_data()
    evaluate_grades(course_data)
