import queue

class Student:
    students = dict() # No duplicates

    def __init__(self, student_id:int, name:str, course:str) -> object:
        self.student_id = student_id
        self.name = name
        self.course = course

    def __repr__(self):
        return f"{self.__class__.__name__}({self._student_id}, {self._name}, {self._course})"

    @property
    def student_id(self):
        return self._student_id

    @property
    def name(self):
        return self._name

    @property
    def course(self):
        return self._course

    @course.setter
    def course(self, course:str):# EmptyCourse
        if not isinstance(course, str):
            raise TypeError("Course must be a 'str'")
        if not course.strip():
            raise ValueError("Course must have a value")
        self._course = course

    @name.setter
    def name(self, name:str):# EmptyName
        if not isinstance(name, str):
            raise TypeError("Name must be a 'str'")
        if not name.strip():
            raise ValueError("Name must have a value")
        self._name = name

    @student_id.setter
    def student_id(self, student_id:int): #InvalidType, NegativeID
        if not isinstance(student_id, int):
            raise TypeError("Student ID must be a 'int'")
        if not student_id >= 0:
            raise ValueError("Student ID can not be negative")
        self._student_id = student_id 

class StudentNode:
    def __init__(self, student:object) -> object:
        self.student = student
        self.left_child = None
        self.right_child = None

class StudentDirectory: # Implement BST
    def __init__(self):
        self.root = None 

    def root_check(self):
        if not self.root:
            return None

    def add_student(self, student_id:int, name:str, course:str):
        name = Student(student_id, name, course)
        Student.students[name.student_id] = (name.name, name.course)
        new_node = StudentNode(name)
        if not self.root:
            self.root = new_node
            return
        current_node = self.root
        while current_node:
            if new_node.student.student_id < current_node.student.student_id:
                if not current_node.left_child:
                    current_node.left_child = new_node
                    return
                current_node = current_node.left_child
            elif new_node.student.student_id > current_node.student.student_id:
                if not current_node.right_child:
                    current_node.right_child = new_node
                    return
                current_node = current_node.right_child
        return

    def search_student(self, student_id:int):
        self.root_check()
        current_node = self.root
        while current_node:
            if student_id == current_node.student.student_id:
                print(f"{'Found Student:':<15}{current_node.student}\n")
                return True
            elif student_id < current_node.student.student_id:
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child
        return None

    def ascending_report(self, initial_vertex): # Depth first search (DFS: print, left, right)
        self.root_check()
        current_node = initial_vertex
        if current_node:
            self.ascending_report(current_node.left_child)
            print(f"{current_node.student}")
            self.ascending_report(current_node.right_child)
        return None

    def level_report(self): # Breath first search (BFS: print levels)
        level = 1
        self.root_check()
        bfs_queue = queue.SimpleQueue()
        bfs_queue.put((level, self.root))
        while not bfs_queue.empty():
            level, current_node = bfs_queue.get()
            print(f"Level: {level} {current_node.student}")
            if current_node.left_child:
                bfs_queue.put((level + 1, current_node.left_child))
            if current_node.right_child:
                bfs_queue.put((level + 1, current_node.right_child))
        return 

# New student entries
student_entries = [
    (100, 'James J. Jones', 'Computer Science'),
    (75, 'Sarah Smith', 'Cybersecurity'),
    (125, 'Michael Brown', 'Data Science'),
    (50, 'Emily Davis', 'Accounting'),
    (90, 'David Wilson', 'Mathematics'),
    (110, 'Olivia Taylor', 'Software Engineering'),
    (150, 'Ethan Moore', 'Information Technology'),
    (25, 'Ava Thomas', 'Network Security'),
    (60, 'Noah Jackson', 'Cloud Computing'),
    (80, 'Sophia', 'Linux Administration'),
    (95, 'Liam Harris', 'Database Systems'),
    (105, 'Isabella Martin', 'Machine Learning'),
    (130, 'Logan Thompson', 'Artifical Intelligence'),
    (175, 'Mia Garcia', 'Data Analytics')
]

# Add students through directory's add student interface
school_directory = StudentDirectory()
for student in student_entries:
    school_directory.add_student(*student)


# Function to print formatted report of student directory
def students_added_report():
    print(f"""\n{'#' * 70}
    \n{'STUDENTS ADDED TO DIRECTORY':^70}
    \n{'#' * 70}""")
    for entry, data in Student.students.items():
        name, course = data
        print(f"""\n{'*' * 50}
        Student Successfully Added 
        Student ID: {entry}
              Name: {name}
            Course: {course}""")


# Search for students by student ID, list includes invalid student IDs for testing
student_search = [100, 57, 25, 120, 175, 999, 105]
for student in student_search:
    exist = school_directory.search_student(student)
    if exist is None:
        print(f"Student ID {student} NOT FOUND\n")

# DFS Ascending Report
school_directory.ascending_report(school_directory.root)
print(' ')

# BFS report by levels
school_directory.level_report()

# Print formatted student directory
students_added_report()

