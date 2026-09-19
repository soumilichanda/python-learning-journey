from datetime import datetime

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

def read_records_from_file():
    records = []
    try:
        with open(FILE_NAME, "r") as file:
            content = file.read().strip()
            if not content:
                return records
            
            raw_blocks = content.split("-" * 30)
            for block in raw_blocks:
                block = block.strip()
                if block:
                    lines = block.split("\n")
                    record_dict = {}
                    marks = []
                    for line in lines:
                        if line.startswith("Added On"):
                            record_dict["added_on"] = line.split(":", 1)[1].strip()
                        elif line.startswith("Name"):
                            record_dict["name"] = line.split(":", 1)[1].strip()
                        elif line.strip().startswith("-"):
                            marks.append(float(line.replace("-", "").strip()))
                        elif line.startswith("Average"):
                            record_dict["average"] = float(line.split(":", 1)[1].strip())
                        elif line.startswith("Grade"):
                            record_dict["grade"] = line.split(":", 1)[1].strip()
                    record_dict["marks"] = marks
                    records.append(record_dict)
    except FileNotFoundError:
        pass
    return records

def rewrite_file(records):
    with open(FILE_NAME, "w") as file:
        for r in records:
            file.write(f"Added On  : {r['added_on']}\n")
            file.write(f"Name      : {r['name']}\n")
            file.write("Marks     :\n")
            for mark in r['marks']:
                file.write(f"  - {mark:.1f}\n")
            file.write(f"Average   : {r['average']:.1f}\n")
            file.write(f"Grade     : {r['grade']}\n")
            file.write("-" * 30 + "\n")

def add_student():
    while True:
        name = input("\nEnter Student Name: ").strip()
        marks = []
        
        for i in range(1, 6):
            while True:
                try:
                    mark = float(input(f"Enter mark {i} (0-100): "))
                    if 0 <= mark <= 100:
                        marks.append(mark)
                        break
                    else:
                        print("❌ Invalid mark! Must be between 0 and 100.")
                except ValueError:
                    print("❌ Invalid input! Please enter a valid number.")
                    
        avg = sum(marks) / len(marks)
        grade = calculate_grade(avg)
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        with open(FILE_NAME, "a") as file:
            file.write(f"Added On  : {now}\n")
            file.write(f"Name      : {name}\n")
            file.write("Marks     :\n")
            for mark in marks:
                file.write(f"  - {mark:.1f}\n")
            file.write(f"Average   : {avg:.1f}\n")
            file.write(f"Grade     : {grade}\n")
            file.write("-" * 30 + "\n")
            
        print(f"\n✅ Record for {name} saved successfully!")
        
        another = input("\nDo you want to add another student? (Y/N): ").strip().upper()
        if another != 'Y':
            break

def view_students():
    records = read_records_from_file()
    if not records:
        print("\nNo student records found.")
        return
    
    print("\n" + "="*30)
    print("      STUDENT RECORDS      ")
    print("="*30)
    for r in records:
        print(f"Added On  : {r['added_on']}")
        print(f"Name      : {r['name']}")
        print("Marks     :")
        for m in r['marks']:
            print(f"  - {m:.1f}")
        print(f"Average   : {r['average']}")
        print(f"Grade     : {r['grade']}")
        print("-" * 30)
        
    print(f"\n📊 Total Students Saved: {len(records)}")

def search_student():
    search_name = input("\nEnter student name to search: ").strip().lower()
    records = read_records_from_file()
    found = False
    
    for r in records:
        if r['name'].lower() == search_name:
            print("\n✅ Student Found:")
            print(f"Added On  : {r['added_on']}")
            print(f"Name      : {r['name']}")
            print(f"Average   : {r['average']}")
            print(f"Grade     : {r['grade']}")
            found = True
            break
            
    if not found:
        print(f"\n❌ No record found for '{search_name}'.")

def delete_student():
    delete_name = input("\nEnter student name to delete: ").strip().lower()
    records = read_records_from_file()
    
    updated_records = [r for r in records if r['name'].lower() != delete_name]
    
    if len(updated_records) < len(records):
        rewrite_file(updated_records)
        print(f"\n🗑️ Record for '{delete_name}' deleted successfully.")
    else:
        print(f"\n❌ No student named '{delete_name}' was found.")

def display_topper():
    records = read_records_from_file()
    if not records:
        print("\nNo student records found.")
        return
        
    topper = max(records, key=lambda x: x['average'])
    
    print("\n" + "🏆 "*5 + "CLASS TOPPER" + " 🏆"*5)
    print(f"Name    : {topper['name']}")
    print(f"Average : {topper['average']:.2f}")
    print(f"Grade   : {topper['grade']}")
    print("🏆 " * 12)

def main():
    while True:
        print("\n--- Student Record Saver ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by Name")
        print("4. Delete Student Record")
        print("5. View Class Topper")
        print("6. Exit")
        
        choice = input("Enter choice (1-6): ").strip()
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            display_topper()
        elif choice == '6':
            print("\nExiting program. Goodbye!")
            break
        else:
            print("Invalid option! Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
    