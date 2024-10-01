def calculate_total_score(scores):
    """Calculates the total score based on the given list of scores."""
    return sum(scores)

def calculate_overall_grade(total_score):
    """Calculates the overall grade based on the total score.

    Assumes a grading scale with thresholds for A, B, C, etc.
    You can adjust these thresholds as needed.
    """
    if total_score >= 90:
        return "A"
    elif total_score >= 80:
        return "B"
    elif total_score >= 70:
        return "C"
    elif total_score >= 60:
        return "D"
    else:
        return "F"

def display_student_details(student_data):
    """Displays the details of a single student."""
    print(f"Name: {student_data['name']}")
    print(f"Student ID: {student_data['student_id']}")
    print(f"Scores: {student_data['scores']}")
    print(f"Total Score: {calculate_total_score(student_data['scores'])}")
    print(f"Overall Grade: {calculate_overall_grade(calculate_total_score(student_data['scores']))}")
    print()

def main():
    students = []
    num_students = int(input("Enter the number of students: "))

    for i in range(num_students):
        name = input("Enter student name: ")
        student_id = input("Enter student ID: ")
        scores = []
        num_subjects = int(input("Enter the number of subjects: "))

        for j in range(num_subjects):
            score = float(input(f"Enter score for subject {j + 1}: "))
            scores.append(score)

        student_data = {
            "name": name,
            "student_id": student_id,
            "scores": scores
        }
        students.append(student_data)

    print("\nStudent Details:")
    for student in students:
        display_student_details(student)

if __name__ == "__main__":
    main()