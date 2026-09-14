from datetime import datetime

# File name as specified in requirements
FILE_NAME = "student_records.txt"

def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "D"

def add_student():
    while True:
        name = input("\nEnter Student Name: ")
        
        # Input 5 marks
        marks = []
        for i in range(1, 6):
            mark = float(input(f"Enter mark {i}: "))
            marks.append(mark)
            
        # Calculations
        avg = sum(marks) / len(marks)
        grade = calculate_grade(avg)
        
        # Mentor's Challenge: Get current date and time
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Save to file using append mode ('a')
        with open(FILE_NAME, "a") as file:
            file.write(f"Added On  : {now}\n")
            file.write(f"Name      : {name}\n")
            file.write("Marks     :\n")
            for mark in marks:
                file.write(f"  - {mark:.1f}\n")
            file.write(f"Average   : {avg:.1f}\n")
            file.write(f"Grade     : {grade}\n")
            file.write("-" * 30 + "\n")
            
        print(f"\n✅ Record for {name} saved to {FILE_NAME} successfully!")
        
        # Mentor's Challenge: Ask whether to add another student (Y/N)
        another = input("\nDo you want to add another student? (Y/N): ").strip().upper()
        if another != 'Y':
            break

def view_students():
    print("\n" + "="*30)
    print("      STUDENT RECORDS      ")
    print("="*30)
    
    try:
        with open(FILE_NAME, "r") as file:
            content = file.read()
            if content.strip():
                print(content)
            else:
                print("No records found in file.")
    except FileNotFoundError:
        print("No student records file found yet. Add a student first!")

def main():
    while True:
        print("\n--- Student Record Saver ---")
        print("1 Add Student")
        print("2 View Students")
        print("3 Exit")
        
        choice = input("Enter choice (1-3): ").strip()
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid input! Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()