import json
from models import Student

class StudentManager:
    def __init__(self):
        self.students = []
        self.file_name = "students.json"
        self.load_data()
        
    def load_data(self):
        try:
            with open(self.file_name, "r") as f:
                data = json.load(f)
                for item in data:
                    student = Student(item["name"], item["roll_no"], item["marks"])
                    
                    self.students.append(student)
                    
        except (FileNotFoundError, json.JSONDecodeError):
            self.students = []
            
    def save_data(self):
        student_list = [s.to_dict() for s in self.students]
        with open(self.file_name, "w") as f:
            json.dump(student_list, f, indent=4)
        print("Data sucessfully saved in file.")
        
    def add_student(self, name, marks):
        roll_no = self.generate_roll_no()
        new_student = Student(name, roll_no, marks)
        self.students.append(new_student)
        print(f"New Student Added! Assigned Roll No: {roll_no}")
        self.save_data()
    
    def search(self, roll_no):
        for s in self.students:
            if s.roll_no == roll_no:
                print("\nStudent mil gaya!\n")
                s.display()
                return
        print("student nhi mila.")
    
    def delete_student(self, roll_no):
        for s in self.students:
            if s.roll_no == roll_no:
                self.students.remove(s)
                self.save_data()
                print(f"Roll no {roll_no} wala student delete ho gaya!")
                return
        print(f"Roll no {roll_no} ka koi student nahi mila!")
        
    def generate_roll_no(self):
        if len(self.students) == 0:
            return 1
        return self.students[-1].roll_no + 1
     
    def display_all(self):
        if len(self.students) == 0:
            print("Abhi koi Student nhi hai.")
            
        else:
            print("\n-------------------List of Students-------------------")
            for s in self.students:
                s.display()
            print("\n------------------------------------------------------")
