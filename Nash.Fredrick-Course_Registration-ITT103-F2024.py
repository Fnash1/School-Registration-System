# No need for 'import self'
print("Welcome to NASHVILLE Course Registration and Payment System\n")

# Predefined students' names
Name = ("Fredrick Nash", "Dwyane Brown", "Shawn Spencer")
Age = 34, 33, 25
balance = 0
Course = {}

# Course class to define the course object
class Course:
    def __init__(self, course_id, name, fee):
        self.course_id = course_id
        self.name = name
        self.fee = fee

# Student class
class Student:
    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.courses = []
        self.balance = 0

    def enroll(self, course):
        if course in self.courses:
            print(f"Student enrolled already in {course.name}.")
        else:
            self.courses.append(course)
            print(f"Student is enrolled successfully in {course.name}")
            self.balance += course.fee

    def get_total_fee(self):
        return sum(course.fee for course in self.courses)

# RegistrationSystem class
class RegistrationSystem:
    def __init__(self):
        self.show_student = {}
        self.show_students_in_course = []
        self.courses = []
        self.students = {}

    def add_course(self, course_id, name, fee):
        course = Course(course_id, name, fee)
        self.courses.append(course)
        print(f"Course '{name}' added successfully.")

    def register_student(self, student_id, name, email):
        if student_id in self.students:
            print("Student already registered.")
            return
        student = Student(student_id, name, email)
        self.students[student_id] = student
        print(f"Student {name} registered successfully")

    def show_courses(self):
        print("\nAvailable Courses:")
        if not self.courses:
            print("No courses available")
            return
        for course in self.courses:
            print(f"ID: {course.course_id} - {course.name} (Fee: ${course.fee})")

    def show_registered_students(self):
        print("\nRegistered Students:")
        if not self.students:
            print("No students are registered.")
            return
        for student_id, student in self.students.items():
            print(f"ID: {student.student_id}, Name: {student.name}")

    def enroll_in_course(self, student_id, course_id):
        try:
            if student_id not in self.students:
                raise ValueError("Student not registered.")

            student = self.students[student_id]
            course = next((c for c in self.courses if c.course_id == course_id), None)

            if not course:
                raise ValueError("Course not found.")

            student.enroll(course)

            # Calculate minimum payment required (40% of the Course Fee)
            min_payment = 0.40 * student.get_total_fee()
            print(f"Minimum payment required: ${min_payment}")

            # Accept payment of at least 40% or in full
            payment = float(input("Enter payment amount: $"))
            if payment == 'total_payment':
                student.balance += payment
                print("Payment successful")
                print(f"Remaining balance: ${student.balance:.2f}")
            else:
                print("Payment added successfully. Thank you")
        except Exception as e:
            print(f"Error: {e}")

    def show_student_in_course_(self, course_id, name):
        print("student in course")
        return
        print(f"ID: {student.student_id}, Name: {student.name}, course: {course_id}")

    def show_enroll_students_in_(self, course_id):
        print(self, 'course_id, name: self.name')

# Main loop for the menu system
def main():
    system = RegistrationSystem()

    choice = 0
    while choice != 9:
        print("*******Menu*******")
        print("1. Show Courses")
        print("2. Add Course")
        print("3. Register Student")
        print("4. Show Students in Course")
        print("5. Show Registered Students")
        print("6. Enroll in Course")
        print("7. Calculate Payment")
        print("8. Check Student balance")
        print("9. Exit")

        try:
            choice = int(input("\nSelect an option:\n"))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue

        if choice == 3:
            student_id = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            email = input("Enter Email: ")
            system.register_student(student_id, name, email)

        elif choice == 2:
            try:
                course_id = int(input("Enter Course ID: "))
                course_name = input("Enter Course Name: ")
                course_fee = float(input("Enter Course Fee: "))
                system.add_course(course_id, course_name, course_fee)
            except ValueError:
                print("Invalid input. Course ID must be in digits.")

        elif choice == 1:
            system.show_courses()

        elif choice == 6:
            student_id = input("Enter Student ID: ")
            try:
                course_id = int(input("Enter Course ID: "))
                system.enroll_in_course(student_id, course_id)
            except ValueError:
                print("Invalid Course ID, Please enter a numerical digit.")

        elif choice == 5:
            system.show_registered_students()

        elif choice == 4:
            try:
                course_id = int(input("Enter Course ID for Students enrolled: "))
                course_name = input("Enter Course name")
                system.show_enroll_students_in_(course_id)
            except ValueError:
                print("Invalid Course ID. Please enter course ID in Digits.")

        elif choice == 7:
            student_id = input("Enter Student ID: ")
            payment = float(input("Enter payment amount: $"))
            if payment <= payment:
                print("Payment successful")
                print(f"Remaining balance: ${student_id.balance:.2f}")
            student_id.balance += (float(input("Enter payment amount: $")))
            print(f"New Balance in self.balance: ")

        elif choice == 8:
            student_id = input("Enter Student ID to check student balance: ")
            if student_id in system.students:
                print(f"Student {system.students[student_id].name} balance: ${system.students[student_id].balance:.2f}")
            else:
                print("Student not found.")

        elif choice == 9:
            print("Exiting Program ")
            break
        else:
            print("Invalid selection. attempt again.")

if __name__ == "__main__":
    main()