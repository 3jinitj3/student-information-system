# Student Information System

A Python-based student directory application built using object-oriented programming and a Binary Search Tree (BST) to manage student records, perform efficient searches, and demonstrate tree traversal algorithms.

---

## Features

- Student record management
- Binary Search Tree (BST) insertion
- Student search by ID
- Depth-First Search (DFS) traversal
- Breadth-First Search (BFS) traversal
- Level-order reporting
- Input validation
- Duplicate student prevention structure
- Queue-based traversal operations

---

## Technologies

- Python
- Object-Oriented Programming (OOP)
- Binary Search Trees (BST)
- Queue Data Structure

---

## Project Structure

### Core Classes

```text
Student
│
├── StudentNode
│
└── StudentDirectory
```

### Responsibilities

#### Student

Represents an individual student record.

Attributes:

- Student ID
- Name
- Course

Features:

- Property validation
- Encapsulation
- Data integrity controls

#### StudentNode

Represents a node in the Binary Search Tree.

Contains:

- Student object
- Left child reference
- Right child reference

#### StudentDirectory

Implements the Binary Search Tree and directory operations.

Supports:

- Student insertion
- Student search
- DFS traversal
- BFS traversal
- Level-order reporting

---

## Concepts Demonstrated

### Object-Oriented Programming

- Encapsulation
- Property Validation
- Class Design
- Object Composition

### Data Structures

- Binary Search Trees (BST)
- Nodes
- Queue

### Algorithms

- Binary Search Tree Search
- Depth-First Search (DFS)
- Breadth-First Search (BFS)
- Level-Order Traversal

---

## Sample Output

### Student Directory Population

screenshots/student_creation.png

### Student Search Results

screenshots/student_search.png

### DFS Traversal (Ascending Report)

screenshots/dfs_traversal.png

### BFS Traversal (Level Report)

screenshots/bfs_levels.png

---

## Example Search Results

```text
Found Student: Student(100, James J. Jones, Computer Science)

Student ID 57 NOT FOUND

Found Student: Student(25, Ava Thomas, Network Security)

Student ID 120 NOT FOUND

Found Student: Student(175, Mia Garcia, Data Analytics)

Student ID 999 NOT FOUND

Found Student: Student(105, Isabella Martin, Machine Learning)
```

---

## Example DFS Traversal

Students are returned in ascending order by Student ID.

```text
Student(25, Ava Thomas, Network Security)
Student(50, Emily Davis, Accounting)
Student(60, Noah Jackson, Cloud Computing)
Student(75, Sarah Smith, Cybersecurity)
Student(80, Sophia, Linux Administration)
Student(90, David Wilson, Mathematics)
Student(95, Liam Harris, Database Systems)
Student(100, James J. Jones, Computer Science)
Student(105, Isabella Martin, Machine Learning)
Student(110, Olivia Taylor, Software Engineering)
Student(125, Michael Brown, Data Science)
Student(130, Logan Thompson, Artificial Intelligence)
Student(150, Ethan Moore, Information Technology)
Student(175, Mia Garcia, Data Analytics)
```

---

## Example BFS Traversal

Students are grouped by tree level.

```text
Level: 1 Student(100, James J. Jones, Computer Science)

Level: 2 Student(75, Sarah Smith, Cybersecurity)
Level: 2 Student(125, Michael Brown, Data Science)

Level: 3 Student(50, Emily Davis, Accounting)
Level: 3 Student(90, David Wilson, Mathematics)
Level: 3 Student(110, Olivia Taylor, Software Engineering)
Level: 3 Student(150, Ethan Moore, Information Technology)

Level: 4 Student(25, Ava Thomas, Network Security)
Level: 4 Student(60, Noah Jackson, Cloud Computing)
Level: 4 Student(80, Sophia, Linux Administration)
Level: 4 Student(95, Liam Harris, Database Systems)
Level: 4 Student(105, Isabella Martin, Machine Learning)
Level: 4 Student(130, Logan Thompson, Artificial Intelligence)
Level: 4 Student(175, Mia Garcia, Data Analytics)
```

---

## Design Considerations

Student records are stored in a Binary Search Tree (BST) keyed by Student ID.

While a Python dictionary would provide average O(1) lookup performance and would likely be preferred for a production-grade student directory, a BST was intentionally implemented to demonstrate:

- Tree insertion
- Binary-search-based retrieval
- Ordered record retrieval
- DFS traversal
- BFS traversal
- Queue usage
- Fundamental data structure implementation

A dictionary is also used to maintain student records and support fast membership checks while preserving the educational value of the BST implementation.

---

## Future Enhancements

- Student deletion
- Course enrollment management
- File persistence
- SQLite integration
- PostgreSQL integration
- Reporting dashboard
- REST API support
- Automated testing with pytest

---

## Author

James Jones

Computer Science Graduate Student

Software Engineering | Python | SQL