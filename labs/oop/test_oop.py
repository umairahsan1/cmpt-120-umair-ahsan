from course import Course
from student import Student


class TestClass:

    def test_00(self):
        student = Student("John", "Doe", "Mathematics")
        assert student is not None

    def test_01(self):
        student = Student("John", "Doe", "Mathematics", [
            Course("Algebra", 104, 3, "A")
        ])
        assert len(student.courses) == 1

    def test_02(self):
        student = Student("John", "Doe", "Mathematics", [
            Course("Algebra", 104, 3, "A")
        ])
        assert student.get_credits() == 3

    def test_03(self):
        student = Student("John", "Doe", "Mathematics")
        student.add_course(Course("Networking & Security", 401, 4, "A"))
        assert student.get_credits() == 4

    def test_04(self):
        student = Student("Kevin", "Hayden", "Computer Science", [
            Course("Intro to Programming", 120, 4, "A"),
            Course("Discrete Math", 220, 4, "B"),
            Course("Russian Literature", 154, 3, "A-"),
            Course("Computer Forensics", 130, 3, "B+")
        ])
        assert student.get_gpa() == 3.5

    def test_05(self):
        student = Student("John", "Doe", "Mathematics")
        student.change_major("Computer Science")
        assert student.major == "Computer Science"
