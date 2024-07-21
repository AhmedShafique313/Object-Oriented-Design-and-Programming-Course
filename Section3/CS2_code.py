class reports:
    def __init__(self, name):
        self.name= name
        self.students_reports ={
            "John": 80.0,
            "Ahmed":95.0,
            "Ita Lauur": 77.0
        }
    
    def attendence_reports(self):
        percentage= self.students_reports.get(self.name)
        return f"{self.name}'s attendence percentage is {percentage}%"

student = input("Enter the name of the student from the list: ")
report1 = reports(student)
print(report1.attendence_reports())