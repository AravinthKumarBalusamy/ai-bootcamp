

class GradeCalculator:

    def __init__(self):
        self.students = {}

    def add_student(self, name):
        if name not in self.students:
            self.students[name] = {
                'math': [],
                'science': [],
                'english': [],
                'history': []
            }
            print(f"Student {name} added successfully.")
        else:
            print(f"Student {name} already exists.")

    def add_grade(self, student_name, subject, grade):
        if student_name not in self.students:
            print(f"Student {student_name} does not exist.")
        else:
            if 0 <= grade <= 100:
                self.students[student_name][subject].append(grade)
                print(f"Grade {grade} added for {student_name} in {subject}.")
            else:
                print(f" Please enter a grade between 0 and 100.")

    def calculate_average(self, grade_list):
        if not grade_list:
            return 0
        return sum(grade_list) / len(grade_list)

    def get_student_average(self, student_name):
        all_grades = []
        for subject_grades in self.students[student_name].values():
            all_grades.extend(subject_grades)
        if not all_grades:
            return 0
        return self.calculate_average(all_grades)

        return 0

    def show_student_report(self, student_name):
        if student_name not in self.students:
            print(f"Student {student_name} not found!")
            return
        print(f"\n📊 Report for {student_name}:")
        print("-" * 40)
        
        for subject, grades in self.students[student_name].items():
            if not grades:
                print(f"{subject.capitalize()}: No grades recorded.")
            else:
                average = self.calculate_average(grades)
                print(f"{subject.capitalize():10}: {grades} → Average: {average:.1f}")
            overall_average = self.get_student_average(student_name)
            print(f"Overall Average for {student_name}: {overall_average:.1f}")

    def list_all_students(self):
        """Show all students with their averages"""
        if not self.students:
            print("No students added yet!")
            return
            
        print("\n👥 All Students:")
        print("-" * 30)
        for student in self.students:
            avg = self.get_student_average(student)
            print(f"{student:15}: {avg:.1f}")


def main():
    calculator = GradeCalculator()
    print("🎓 Smart Grade Calculator")
    print("Learn list operations used in AI data processing!")
    while True:
        print("\n1. Add Student")
        print("2. Add Grade")
        print("3. Student Report")
        print("4. All Students")
        print("5. Exit")
        choice = input("Choose option (1-5): ")
        if choice == '1':
            name = input("Enter student name: ").strip()
            calculator.add_student(name)
        elif choice == '2':
            name = input("Enter student name: ").strip()
            subject = input("Enter subject (math/science/english/history): ").strip().lower()
            try:
                grade = float(input("Enter grade (0-100): "))
                calculator.add_grade(name, subject, grade)
            except ValueError:
                print("Please enter a valid number!")
        elif choice == '3':
            name = input("Enter student name: ").strip()
            calculator.show_student_report(name)
            
        elif choice == '4':
            calculator.list_all_students()
            
        elif choice == '5':
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()