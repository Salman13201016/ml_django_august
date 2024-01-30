class Student:
  #instance based variable #class level variable - property

  # name = "Salman"
  # roll = 16

  # def ins_func(self):
  #   self.name="himu"

  def __init__(self,name,password):
    self.name = name
    self.password = password
    
  #   print("this is a constructor")

  def check_login(self):
    if(self.name=="salman" and self.password=="12345678"):
      print("you have logged in successfully")
    else:
      print("failed")
  

  # def get_study(self):
  #   return self.hours

class Student_child(Student):
  def __init__(self,cname,cpassword,email):
    # print(cname,cpassword)
    super().__init__(cname,cpassword)
    self.email = email 
  def welcome(self):
    print(self.name,self.password,self.email)


obj1 = Student_child("salman","12345678",'s@gmail.com')
obj1.welcome()

# obj1 = Student()
# obj2 = Student()

# print(obj1.name)
# obj2.ins_func()

# print(obj2.name)

# stu_obj = Student("salman","12345678")  #instance of student class
# stu_obj.check_login()

# # print(stu_obj.name, stu_obj.roll)
# number_of_hours = 10
# stu_obj.set_study(10)

# print(stu_obj.get_study())
