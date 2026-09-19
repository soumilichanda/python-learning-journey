import numpy as np

def analyze_student_performance():
    # Rows = Students (4), Columns = Subjects (3)
    marks = np.array([
        [85, 78, 92],
        [67, 74, 70],
        [90, 88, 95],
        [56, 62, 60]
    ])

    print("Class Average :", np.mean(marks))
    print("Highest Mark  :", np.max(marks))
    print("Lowest Mark   :", np.min(marks))

    # Row-wise reduction (each student's average across columns)
    student_averages = np.mean(marks, axis=1)
    for i, avg in enumerate(student_averages, start=1):
        print(f"Student {i} Average : {avg:.2f}")

    # Column-wise reduction (each subject's average across rows)
    subject_averages = np.mean(marks, axis=0)
    for j, avg in enumerate(subject_averages, start=1):
        print(f"Subject {j} Average : {avg:.2f}")

if __name__ == "__main__":
    analyze_student_performance()