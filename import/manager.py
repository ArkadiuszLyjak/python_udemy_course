from user_file import Employee


class Manager(Employee):
    def __init__(self, name, age, salary, department):
        """
        Initialize a Manager object.

        Parameters
        ----------
        name : str
            The employee's name.
        age : int
            The employee's age.
        salary : float
            The employee's salary.
        """
        # User.__init__(self, name, age)
        Employee.__init__(self, name, age, salary)
