
sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))
sub4 = float(input("Enter marks for Subject 4: "))
sub5 = float(input("Enter marks for Subject 5: "))


total = sub1 + sub2 + sub3 + sub4 + sub5
average = total / 5

if average >= 90:
    grade = "Grade A"
elif average >= 75:
    grade = "Grade B"
elif average >= 60:
    grade = "Grade C"
else:
    grade = "Grade D"
print("\n--- Student Performance Summary ---")
print("Total Marks:", total)
print("Average Marks:", average)
print("Final Grade:", grade)