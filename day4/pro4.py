class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks  # List of 5 marks

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)

    def calculate_grade(self):
        avg = self.calculate_average()
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 60:
            return "C"
        else:
            return "D"

    def display_report(self):
        avg = self.calculate_average()
        grade = self.calculate_grade()
        print("\n" + "=" * 35)
        print("        STUDENT REPORT CARD        ")
        print("=" * 35)
        print(f"Name        : {self.name}")
        print(f"Roll Number : {self.roll_number}")
        print(f"Marks       : {self.marks}")
        print(f"Average     : {avg:.2f}")
        print(f"Grade       : {grade}")
        print("=" * 35)

    def save_to_file(self, filename="report_cards.txt"):
        avg = self.calculate_average()
        grade = self.calculate_grade()
        
        # Save OOP object report into external text file
        with open(filename, "a") as file:
            file.write("=" * 35 + "\n")
            file.write("        STUDENT REPORT CARD        \n")
            file.write("=" * 35 + "\n")
            file.write(f"Name        : {self.name}\n")
            file.write(f"Roll Number : {self.roll_number}\n")
            file.write(f"Marks       : {self.marks}\n")
            file.write(f"Average     : {avg:.2f}\n")
            file.write(f"Grade       : {grade}\n")
            file.write("=" * 35 + "\n\n")
        print(f"\nReport Card successfully saved to '{filename}'!")


# Main program execution
if __name__ == "__main__":
    name = input("Enter Student Name: ")
    roll = input("Enter Roll Number: ")
    
    marks = []
    print("\nEnter marks for 5 subjects:")
    for i in range(1, 6):
        score = float(input(f"  Subject {i}: "))
        marks.append(score)

    # Instantiate the OOP Student object
    student1 = Student(name, roll, marks)

    # Call instance methods
    student1.display_report()
    student1.save_to_file()