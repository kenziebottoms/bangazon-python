# Classes

## Instructions

- [x] Copy this `Company` class into your module.
    ```py
    class Company(object):
        """This represents a company in which people work"""

        def __init__(self, company_name, date_founded):
            self.company_name = company_name
            self.date_founded = date_founded

        def get_company_name(self):
            """Returns the name of the company"""

            return self.company_name

        # Add the remaining methods to fill the requirements above
    ```

- [x] Create a class that contains information about employees of a company and define methods to get/set
    - [x] employee name,
    - [x] job title,
    - [x] and start date.

- [ ] Consider the concept of [aggregation](../FND_11_INHERIT_COMPOSE_AGGREGATE.md#aggregation), and modify the `Company` class so that you assign employees to a company.

- [ ] Create a company, and three employees, and then assign the employees to the company.