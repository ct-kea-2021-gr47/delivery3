# domain Identity and Access Management
class User:

    user_id = 1

    def __init__(self, username, password, role_id=None):
        self.username = username
        self.password = password
        self.role_id = role_id
        self.id = User.user_id
        User.user_id += 1

    def change_password(self, new_password):
        self.password = new_password

    def login(self, username, password):
        pass

    class Role:

        role_id = 1

        def __init__(self, role_name):
            self.role_name = role_name
            self.id = User.Role.role_id
            User.Role.role_id += 1


# domain Customer Relationship Management
class Customer:

    users = []
    projects = []
    customer_id = 1

    def __init__(self, name):
        self.name = name
        self.id = Customer.customer_id
        Customer.customer_id += 1

    def add_user(self, user_id):
        self.users.append(user_id)

    def add_project(self, project_id):
        self.projects.append(project_id)

    def delete(self):
        del self

    class Address:

        address_id = 1

        def __init__(self, name1, zipcode, city, name2=""):
            self.name1 = name1
            self.name2 = name2
            self.zipcode = zipcode
            self.city = city
            self.id = Customer.Address.address_id
            Customer.Address.address_id += 1


# domain Product
class Session:

    session_id = 1

    def __init__(self, session_id, duration, mode, user_id):
        self.id = session_id
        self.duration = duration
        self.mode = mode
        self.user_id = user_id
        self.id = Session.session_id
        Session.session_id += 1

    def start(self):
        pass

    def add_measurements(self):
        pass

    def end(self):
        pass

    class Measure:

        measure_id = 1

        def __init__(self, alpha, beta, gamma, delta, theta):
            self.alpha = alpha
            self.beta = beta
            self.gamma = gamma
            self.delta = delta
            self.theta = theta
            self.id = Session.Measure.measure_id
            Session.Measure.measure_id += 1

        def measure(self):
            pass


class Profile:

    profile_id = 1

    def __init__(self, measurement):
        self.measurement = measurement
        self.id = Profile.profile_id
        Profile.profile_id += 1

    def get_calculation(self):
        pass

    def get_measurement(self):
        pass

    class Calculation:

        calculation_id = 1

        def __init__(self):
            self.id = Profile.Calculation.calculation_id
            Profile.Calculation.calculation_id += 1

        def calculate(self):
            pass


# domain Project
class Project:

    project_id = 1

    def __init__(self, name, startdate, enddate):
        self.name = name
        self.startdate = startdate
        self.enddate = enddate
        self.id = Project.project_id
        Project.project_id += 1

    def delete_project(self):
        pass

    def end_project(self):
        pass

    def edit_project(self, project_id):
        pass



# domain Invoice
class Invoice:

    invoice_id = 1

    def __init__(self, invoicenr, date, total, due_date, project_id):
        self.invoicenr = invoicenr
        self.date = date
        self.total = total
        self.due_date = due_date
        self.project_id = project_id
        self.id = Invoice.invoice_id
        Invoice.invoice_id += 1
