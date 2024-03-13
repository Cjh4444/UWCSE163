# Write your solution to main.py here!
from student import Student


def main():
    pablo = Student(1551515, "CP4/lesson13/practice-student-class/pablo.txt")
    arlo = Student(1231231, "CP4/lesson13/practice-student-class/arlo.txt")
    print(
        f"{pablo.get_name()} {pablo.get_student_number()}"
        + f' {pablo.get_credits_for("CSE163")}'
    )
    print(
        f"{arlo.get_name()} {arlo.get_student_number()}"
        + f' {arlo.get_credits_for("CSE163")}'
    )


if __name__ == "__main__":
    main()
