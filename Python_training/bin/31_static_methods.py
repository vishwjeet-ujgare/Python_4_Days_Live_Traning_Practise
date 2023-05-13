"""
Static Methods
"""


class Employee:
    @staticmethod
    def compute_avg_salary(sal1, sal2):
        # - No where we are using instance object here,
        #   so 'self/instance-object' is not require
        # - Now, unnc=eccessarilty we are keeping instance-object/self here
        avg_salary = (sal1 + sal2)/2
        return avg_salary


e1 = Employee()
e2 = Employee()

s1 = 10000
s2 = 20000
avg_salary = e1.compute_avg_salary(s1, s2)
# since 'compute_avg_salary' is static method, 'e1' WILL NOT GO AS 1st parmeter
print("avg_salary:", avg_salary)


