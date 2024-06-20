import os.path

# File path to store student data
file_path = "student_data.txt"

# Function to add a new student
def add_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    grade = input("Enter student grade: ")
    with open(file_path, "a") as file:
        file.write(f"{student_id},{name},{age},{grade}\n")
    print("Student added successfully.")

# Function to view all students
def view_students():
    if not os.path.exists(file_path):
        print("No student data available.")
        return
    with open(file_path, "r") as file:
        print("Student ID\tName\t\tAge\tGrade")
        for line in file:
            student_id, name, age, grade = line.strip().split(',')
            print(f"{student_id}\t\t{name}\t\t{age}\t{grade}")

# Function to search for a student by ID
def search_student():
    student_id = input("Enter student ID to search: ")
    with open(file_path, "r") as file:
        for line in file:
            data = line.strip().split(',')
            if data[0] == student_id:
                print("Student found:")
                print("Student ID\tName\t\tAge\tGrade")
                print(f"{data[0]}\t\t{data[1]}\t\t{data[2]}\t{data[3]}")
                return
        print("Student not found.")

# Main function
def main():
    while True:
        print("\nStudent Information System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
