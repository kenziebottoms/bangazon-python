class Company(object):
    """This represents a company in which people work"""

    def __init__(self, company_name, date_founded):
        self.company_name = company_name
        self.date_founded = date_founded
        self.employees = set()

    def get_company_name(self):
        """Returns the name of the company"""
        return self.company_name


class Employee(object):
    """This represents the people who work for a company"""

    def __init__(self, first_name, last_name, job_title, start_date):
        self.first_name = first_name
        self.last_name = last_name
        self.start_date = start_date
        self.job_title = job_title

    def get_name(self):
        return self.first_name + ' ' + self.last_name

    def set_name(self, first, last):
        self.first_name = first
        self.last_name = last

    def get_start_date(self):
        return self.start_date

    def set_start_date(self, start_date):
        self.start_date = start_date

    def get_title(self):
        return self.job_title

    def set_title(self, job_title):
        self.job_title = job_title


if __name__ == '__main__':
    NSS = Company('Nashville Software School', '23-April-2016')

    joe = Employee('Joe', 'Shepherd', 'Front End Instructor', '24-may-2018')
    steve = Employee('Steve', 'Brownlee', 'Back End Instructor', '23-may-2018')
    brenda = Employee('Brenda', 'Long', 'UI/UX Instructor', '18-may-2018')

    NSS.employees.update([joe, steve, brenda])

    employees = list(NSS.employees)

    print map(lambda e: e.get_name(), employees)
