# Write your Student class here
class Student:
    student_number: int
    name: str
    classes: dict[str, int]

    def __init__(self, student_number: int, student_file: str) -> None:
        self.student_number = student_number
        self.name = student_file.split("/")[-1].split(".")[0]
        with open(student_file) as f:
            self.classes = {
                line.split(" ")[0].strip(): int(line.split(" ")[1])
                for line in f
            }

    def get_name(self) -> str:
        return self.name

    def get_student_number(self) -> int:
        return self.student_number

    def get_credits_for(self, class_name: str) -> int:
        return self.classes[class_name] if class_name in self.classes else None

    def get_classes(self) -> list:
        return list(self.classes)
