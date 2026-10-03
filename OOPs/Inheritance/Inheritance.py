class emp:
    company = "infosys"
    def show(self):
        print("The Employee is of infosys")

class dept(emp):
    dept_name = "it"

dept1 = dept()

print(dept1.company)
dept1.show()
print(dept1.dept_name)