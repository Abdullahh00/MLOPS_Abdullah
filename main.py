class mlops:
    def __init__(self,totalStudents):
            self.totalStudents=totalStudents

    def getTotalStudents(self):
          return self.totalStudents
    
    def addStudents(self):
          self.totalStudents=self.totalStudents+1

        
    def removeStudent(self):
          self.totalStudents=self.totalStudents-1
    
    def getCLassName(self):
          return "MAchine Learning Operations (CS_B)"
    

# mlops_class = mlops(5)
# mlops_class.addStudents()
# mlops_class.removeStudent()
# print(mlops_class.getTotalStudents())
# print(mlops_class.getCLassName())