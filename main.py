from manager import StudentManager

manager = StudentManager()
try:        
    while True:
        print("\n----------------Student Management System------------------")
        print("1. Add Student")
        print("2. view all Student")
        print("3. Search Student by Roll No")
        print("4. Delete Student")
        print("5. Exit")

        
        try:
            choice = int(input("Enter your choice: ").strip())
        except ValueError:
            print("Enter a valid option only.")
            continue
        if choice == 1:
            while True:
                try:
                    name = input("Enter full name of student: ").strip().title()
                    
                    if not name or name.isdigit(): 
                        print("Enter a valid name.")
                        continue
                    
                    marks = int(input("Enter marks: ").strip())
                    
                    manager.add_student(name, marks)
                    break
                except ValueError:
                    print("Enter only numbers.")
                    
        elif choice == 2:
            manager.display_all()
        
        elif choice == 3:
            try:
                r_no = int(input("Enter roll no to search: ").strip())
                manager.search(r_no)
            except ValueError:
                print("Roll number sirf number hona chahiye!")
        elif choice == 4:
            try:
                r_no = int(input("Enter roll no to delete: ").strip())
                manager.delete_student(r_no)
            except ValueError:
                print("Roll number sirf number hona chahiye!")
                
        elif choice == 5:
            print("Thanks for using.")
            break
        else:
            print("invalid choice! Enter only 1, 2, 3, 4 or 5.")
except KeyboardInterrupt:
    print("\n\nStopped by user.")
    