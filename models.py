class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
        
    def display(self):
        print(f"Roll no: {self.roll_no} | Name: {self.name} | Marks: {self.marks}")
        
    def to_dict(self):
        return{
            "name": self.name,
            "roll_no" : self.roll_no,
            "marks" : self.marks}