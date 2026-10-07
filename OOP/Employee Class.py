class Employee():
    def __init__(self, name, id, basicSalary, hra, da, tax):
        self.name = name
        self.id = id
        self.basicSalary = basicSalary
        self.hra = hra
        self.da = da
        self.tax = tax
        print("Employee class object is created")

    def grossSalary(self):
        hraAmount = self.hra / 100
        daAmount = self.da / 100
        totalSal = self.basicSalary + hraAmount + daAmount
        return totalSal

    def netSalary(self):
        grossAmount = self.grossSalary()
        final = grossAmount - (grossAmount * self.tax)
        #print(f"Salary: {self.final}")
        return final

    def details(self):
        print(f"""
Name: {self.name}
ID: {self.id}
Base Salary: {self.basicSalary}
HRA: {self.hra}
DA: {self.da}
Gross Salary: {self.grossSalary()}
Salary: {self.netSalary()}
        """)

#e = Employee("Bob", "7913245", 50000, 20, 13, 0.13)
#e.grossSalary()
#e.netSalary()
#e.details()

class Manager(Employee):
    def __init__(self, name, id, basicSalary, hra, da, tax, department, managementAllowance):
        self.name = name
        self.id = id
        self.basicSalary = basicSalary
        self.hra = hra
        self.da = da
        self.tax = tax
        self.department = department
        self.allowance = managementAllowance
 

    # def details(self):
    #     print(f"""
    #     Department: {self.department}
    #     Management Allownace: {self.allowance}
    #     """)

class Developer(Employee):
    def __init__(self, name, id, basicSalary, hra, da, tax, progLanguage, projectAllowance):
        self.name = name
        self.id = id
        self.basicSalary = basicSalary
        self.hra = hra
        self.da = da
        self.tax = tax
        self.language = progLanguage
        self.allowance = projectAllowance

    def grossSalary(self):
            self.grossSalary(self) 
            totalSal += self.allowance 

    # def details(self): 
    #     print(f"""
    #     Programming Language: {self.departement}
    #     Project Allownace: {self.allowance}
    #     """)

priya = Manager("Priya", "M101", 50000, 20, 10, 0.10, "Sales", 10000)
rahul = Manager("Rahul", "D101", 40000, 20, 10, 0.10, "Python", 5000)
priya.details()
    