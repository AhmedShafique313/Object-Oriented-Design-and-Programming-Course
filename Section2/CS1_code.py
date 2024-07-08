class data:
    name=''
    age=0
    position=''
    years=0
    def calculate_salary(self):
        if self.position == 'Engineer':
            salary = 100000 * self.years /2
            return salary
        elif self.position == 'Manager':
            salary = 125000 * self.years / 3
            return salary
        elif self.position == 'Employee':
            salary = 45000 * self.years / 4
            return salary

def no_employees():
    emp_data = data()
    emp_data.name = input('Enter the name of Employe: ')
    emp_data.age = int(input(f'Enter the age of {emp_data.name}: '))
    emp_data.position = input(f'Enter the position of {emp_data.name} in company: ')
    emp_data.years = int(input(f'Enter years of experience as a {emp_data.position}: '))

    # printing statements
    print(f'Name: {emp_data.name}, Age: {emp_data.age}, Postion: {emp_data.position}, Years of experience: {emp_data.years}, Salary: ', emp_data.calculate_salary())
    




no_employees()