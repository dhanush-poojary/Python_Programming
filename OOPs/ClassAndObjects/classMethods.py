class emp:
    company = "infosys"
    @classmethod  #it is a decorator that means instead of reffering to instance's class attribute just reffer to class's attribute
    def show(cls):
        print(f"The Employee is of {cls.company}")

Emp = emp()
print(Emp.company)

Emp.company = "Juego"
print(Emp.company)

Emp.show()
