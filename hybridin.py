
class University:
    def __init__(self,uni_name):
        self.uni_name=uni_name
    def Showdetails(self):
        print(f"university name is:{self.uni_name}")
class Course(University):
    def __init__(self,uni_name,c_name):
        University.__init__(self,uni_name)
        self.c_name=c_name
    def Showdetails_C(self):
        print(f"university name:{self.uni_name} and course name:{self.c_name}")
class Branch(University):
    def __init__(self,uni_name,b_name):
        University.__init__(self,uni_name)
        self.b_name=b_name
    def Showdetails_B(self):
        print(f"university name:{self.uni_name} and branch is:{self.b_name}")
class Stu(Branch,Course,University):
    def __init__(self,uni_name,c_name,b_name,s_name):
        Branch.__init__(self,uni_name,b_name)
        Course.__init__(self,uni_name,c_name)
        self.s_name=s_name
    def Showdetails_S(self):
         print(f"student name:{self.s_name} and branch is :{self.b_name} and course is :{self.c_name} and university is :{self.uni_name}")
class Fac(Branch):
    def __init__(self,uni_name,b_name,f_name):
        Branch.__init__(self,uni_name,b_name)
        University.__init__(self,uni_name)
        self.f_name=f_name
    def Showdetails_F(self):
        print(f"faculty name is:{self.f_name} and branch is :{self.b_name} and university is :{self.uni_name}")
s1=Stu("askw","btech","cse","leela")
s1.Showdetails_S()
print(Stu.mro())
f1=Fac("askw","cse","sridevi")
f1.Showdetails_F()
b1=Branch("askw","cse")
b1.Showdetails_B()
c1=Course("askw","btech")
c1.Showdetails_C()
