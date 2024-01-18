import json
from datetime import datetime
from IEmploye import IEmploye
from  exame2   import IR
from Employe1 import Employe

from Agent import Agent
from  Formature   import Formature

class Company:
    def __init__(self):
        self.employees = []

    def display_employees(self):
        for emp in self.employees:
            print(emp)

    def add_employee(self, employee):
        self.employees.append(employee)

    def delete_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
            print(f"{employee.mtle} - {employee.nom} has been removed.")
        else:
            print("Employee not found.")

    def modify_employee(self, old_employee, new_employee):
        if old_employee in self.employees:
            index = self.employees.index(old_employee)
            self.employees[index] = new_employee
            print(f"{old_employee.mtle} - {old_employee.nom} has been modified.")
        else:
            print("Employee not found.")

    def save_to_json(self, filename):
        data = {"employees": []}
        for emp in self.employees:
            data["employees"].append({
                "mtle": emp.mtle,
                "nom": emp.nom,
                "dateNaissance": emp.dateNaissance.strftime("%Y-%m-%d"),
                "dateEmbuche": emp.dateEmbuche.strftime("%Y-%m-%d"),
                "salaireBase": emp.salaireBase,
                # Add other employee-specific attributes here
            })

        with open(filename, 'w') as json_file:
            json.dump(data, json_file)
        print(f"Data saved to {filename}.")

class TestCompany:
    def __init__(self):
        self.company = Company()

    def run_tests(self):
        emp1 = Agent("MT001", "John Doe", "1990-01-01", "2020-01-01", 50000, 2000)
        emp2 = Formature("MT002", "Jane Smith", "1985-05-15", "2018-03-20", 45000, 10)

        self.company.add_employee(emp1)
        self.company.add_employee(emp2)

        print("Displaying Employees:")
        self.company.display_employees()

        emp3 = Agent("MT003", "Alice Brown", "1988-09-30", "2015-06-10", 60000, 2500)
        self.company.add_employee(emp3)

        print("\nAfter Adding New Employee:")
        self.company.display_employees()

        self.company.delete_employee(emp2)

        print("\nAfter Deleting Employee:")
        self.company.display_employees()

        emp4 = Formature("MT004", "Bob Johnson", "1992-12-20", "2019-08-05", 48000, 15)
        self.company.modify_employee(emp1, emp4)

        print("\nAfter Modifying Employee:")
        self.company.display_employees()

        self.company.save_to_json("employees.json")

if __name__ == "__main__":
    test_company = TestCompany()
    test_company.run_tests()
