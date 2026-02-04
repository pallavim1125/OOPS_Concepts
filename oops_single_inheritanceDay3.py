# Single inheritance

class father:
    def __init__(self,surname,father_name):
        self.surname=surname
        self.father_name=father_name
    def display_surname(self):
        print("Surname:",self.surname)
    def display_father_name(self):
        print("Father Name:",self.father_name)        
        
class son(father):
    def __init__(self,name,surname,father_name):
        super().__init__(surname,father_name)
        self.name=name
    def display_name(self):
        print("Son Name:",self.name)

child_obj=son("John","K","Rajesh")
child_obj.display_father_name()
child_obj.display_surname()
child_obj.display_name()