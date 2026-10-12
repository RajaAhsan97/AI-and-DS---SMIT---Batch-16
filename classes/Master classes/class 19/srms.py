student_records = []

# add student 
def add_student():
    """
        This function will add student data to records:
        
        INPUT:  name, rollno, course, marks 
    """
    name = input("Enter name: ")
    rollno = input("Enter rollno: ")
    course = input("Enter course: ")
    marks = int(input("Enter marks: "))
    
    student = {
        "Name": name,
        "rollno": rollno,
        "course": course,
        "marks": marks
    }

    student_records.append(student)

# displayh all students
def display_record():
    if not student_records:
        print("Records are empty")
    else:
        for student in student_records:
            print("-------------------------------")
            print(f"Student Record:")
            for key, value in student.items():
                print(f"{key}: {value}")
            print("--------------------------------")

# search student --> function definition
def search_student(roll_no):
    if not student_records:
        print("Unable to search in empty records")
    else:
        for student in student_records:
            if student["rollno"] == roll_no:
                for key, value in student.items():
                    print(f"{key}: {value}")

# update student marks
def update_marks(search_rollno):
    if not student_records:
        print("Unable to upadate marks in empty records")
    else:
        for index, student in enumerate(student_records):
            if student["rollno"] == search_rollno:
                new_marks = int(input("Enter marks to update:"))

                student_records[index].update({"marks": new_marks})

                print("Marks updated successfully")

# delete record
def delete_record(roll_no):
    if not student_records:
        print("Unable to delete in empty records")
    else:
        for student in student_records:
            if student["rollno"] == roll_no:
                student_records.remove(student)
                print("Remove successfully")