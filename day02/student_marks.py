# List to store all student records in memory
students = []

def add_student():
    name = input("Enter student name: ")
    
    # Collecting marks for 5 subjects
    marks = []
    for i in range(1, 6):
        score = float(input(f"Enter marks for Subject {i}: "))
        marks.append(score)
        
    student = {
        "name": name,
        "marks": marks
    }
    
    students.append(student)
    print(f"\n✅ {name} added successfully!\n")


def calculate_average(marks):
    return sum(marks) / len(marks)


def display_students():
    if not students:
        print("\nNo student records found.\n")
        return
        
    print("\n" + "="*35)
    print("      STUDENT RESULT RECORDS      ")
    print("="*35)
    
    for s in students:
        avg = calculate_average(s["marks"])
        
        # Simple grading based on average
        if avg >= 90:
            grade = "Grade A"
        elif avg >= 75:
            grade = "Grade B"
        elif avg >= 60:
            grade = "Grade C"
        else:
            grade = "Grade D"
            
        print(f"Name    : {s['name']}")
        print(f"Total   : {sum(s['marks'])}")
        print(f"Average : {avg:.2f}")
        print(f"Grade   : {grade}")
        print("-" * 35)


def main():
    while True:
        print("\n--- Student Result Management ---")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Exit")
        
        choice = input("Enter choice (1-3): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please select 1, 2, or 3.")

# Run the program
if __name__ == "__main__":
    main()