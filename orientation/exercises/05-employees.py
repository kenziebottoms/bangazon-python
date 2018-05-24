class Company(object):
    """This represents a company in which people work"""

    def __init__(self, company_name, date_founded):
        self.company_name = company_name
        self.date_founded = date_founded

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
        return self.first_name, self.last_name
    
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