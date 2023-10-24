class Students:
    def __int__(self,name,course,gender,age):
        self.name = name
        self.course=course
        self.gender=gender
        self.age=age

    def display(self):
        print("Name: %s \n Course: %s\nGender:%s\nAge: %s" % (self.name, self.course, self.gender, self.age))
 display