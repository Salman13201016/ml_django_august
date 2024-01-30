name = "salman"
prod_name = ["n1","n2","n3"]
prod_details = {"name":"p1","price":100}

print(len(name))
print(len(prod_name))
print(len(prod_details))


class Student:
    def action(self):
        print("Student can read or write")


class Teacher:
    def action(self):
        print("Teacher Teaches Students")


obj1 = Student()
obj2 = Teacher()

obj1.action()
obj2.action()