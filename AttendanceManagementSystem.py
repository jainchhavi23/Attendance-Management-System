import datetime as d
operations = """
1. Add Student
2. View Student
3. Update Student
4. Delete Student
5. Mark Attendance
6. Update Attendance
7. View Attendance(Date-Wise)
8. Student Attendance Report
9. Exit
"""
def add_student():
    roll_no = input("Enter Student RollNO: ")
    name = input("Enter Student Name: ")
    course = input("Enter Student Course: ")
  
    with open("studentdata.txt","a") as f:
        f.write(f"{roll_no},{name},{course}\n")
        print("Data Saved Sucessfully.")   

def view_student():
    try:
        with open("studentdata.txt","r") as f:
            print("Student Records")
            print(f.read())
    except FileNotFoundError:
        print("File not found ")

def update_student():
    student_id = input("Enter Student ID to update: ")
    found = False
    try:
       with open("studentdata.txt","r") as f:
            lines = f.readlines()        
       with open("studentdata.txt","w") as f:
           for line in lines:
             data = line.strip().split(",")
             if data[0] == student_id:
                found = True
                name = input("Enter New Name: ")
                course = input("Enter New Course: ")
                f.write(f"{student_id},{name},{course}\n")
             else:
                f.write(line)
       if found:
            print("Record updated successfully")
       else:
            print("Record not found")
    except FileNotFoundError:
        print("File not found")

def delete_student():
    roll_no = input("Enter Student RollNo to delete: ")
    found = False
    try:
       with open("studentdata.txt","r") as f:
         lines = f.readlines()
    
       with open("studentdata.txt","w") as f:
          for line in lines:
            data = line.strip().split(",")
            if data[0] == roll_no:
               found = True
               continue   
            f.write(line) 
       if found:
           print("Record deleted successfully ")
       else:
           print("Record not found ")    
    except FileNotFoundError:
        print("File not found ")

def mark_attendance():
    today = d.datetime.now().strftime("%Y-%m-%d")
    try:
        with open("studentdata.txt","r") as f:
         students = f.readlines()
        with open("Attendance.txt", "a") as f:
            for student in students:
                data = student.strip().split(",")
                roll_no = data[0]
                name = data[1]
                status = input(f"{name} ({roll_no}) P/A: ").upper()
                f.write(f"{today},{roll_no},{status}\n")
            print("Attendance Marked Successfully.")  
    except FileNotFoundError:
        print("Student File not found ")

def update_attendance():
    input_date = input("Enter date (YYYY-MM-DD): ")
    roll_no = input("Enter Roll No: ")
    found = False
    try:
        with open("Attendance.txt", "r") as f:
            lines = f.readlines()
        with open("Attendance.txt", "w") as f:
            for line in lines:
                data = line.strip().split(",")
                if data[0] == input_date and data[1] == roll_no:
                    found = True
                    new_status = input("Enter new status P/A: ").upper()
                    f.write(f"{input_date},{roll_no},{new_status}\n")
                else:
                    f.write(line)
        if found:
            print("Attendance Updated")
        else:
            print("Record Not Found")
    except FileNotFoundError:
        print("Attendance file not found")

def view_attendance():
    input_date = input("Enter date (YYYY-MM-DD): ")
    found = False
    try:
        with open("Attendance.txt", "r") as f:
            for line in f:
                data = line.strip().split(",")
                if data[0] == input_date:
                    print(line.strip())
                    found = True
        if not found:
            print("No record found for this date")
    except FileNotFoundError:
        print("File not found")

def student_attendance_report():
    roll_no = input("Enter Roll No: ")
    total = 0
    present = 0
    try:
        with open("Attendance.txt", "r") as f:
            for line in f:
                data = line.strip().split(",")
                if data[1] == roll_no:
                    total += 1
                    if data[2] == "P":
                        present += 1
        if total > 0:
            percentage = (present / total) * 100
            print("Total Students:", total)
            print("Present:", present)
            print("Absent:", total - present)
            print("Attendance %:", round(percentage, 2))
        else:
            print("No attendance record found")
    except FileNotFoundError:
        print("File not found")

print(operations)
while True:
    try:
        oper = int(input("Enter operations in the form of(1,2,3...): "))
    except ValueError:
        print("Enter operations in the form of(1,2,3...):")
        continue
    if oper == 1:
        print("Add Student:")
        add_student()
    elif oper == 2:
        print("View Student")
        view_student()
    elif oper == 3:
        print("Update Student")
        update_student()
    elif oper == 4:
        print("Delete Student")
        delete_student()
    elif oper == 5:
        print("Mark Attendance")
        mark_attendance()
    elif oper == 6:
        print("Update Attendance")
        update_attendance()
    elif oper == 7:
        print("View Attendance")
        view_attendance()
    elif oper == 8:
        print("Student Attendance Report")
        student_attendance_report()
    elif oper == 9:
        print("Exit Program")
        break
    else:
        print("Enter Valid Operation Number")
    