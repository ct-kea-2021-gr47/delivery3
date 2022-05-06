# domain Identity and Access Management
class User:

    User_ID = 1

    def __init__(self, username, password, role_id="default"):
        self.username = username
        self.password = password
        self.role_id = role_id
        self.id = User.User_ID
        User.User_ID += 1

    def change_password(self, new_password):
        self.password = new_password

    def login(self, username, password):
        pass

    class Role:

        Role_ID = 1

        def __init__(self, role_name):
            self.role_name = role_name
            self.id = User.Role.Role_ID
            User.Role.Role_ID += 1


# domain Customer Relationship Management
class Customer:

    users = []
    projects = []
    Customer_ID = 1

    def __init__(self, name):
        self.name = name
        self.id = Customer.Customer_ID
        Customer.Customer_ID += 1

    def add_user(self, User_ID):
        self.users.append(User_ID)

    def add_project(self, Project_ID):
        self.projects.append(Project_ID)

    def delete():
        pass

    class Address:

        Address_ID = 1

        def __init__(self, name1, zipcode, city, name2=""):
            self.name1 = name1
            self.name2 = name2
            self.zipcode = zipcode
            self.city = city
            self.id = Customer.Address.Address_ID
            Customer.Address.Address_ID += 1


# domain Product
class Product:

    Product_ID = 1

    def __init__(self, session_id, duration, mode, User_ID):
        self.session_id = session_id
        self.duration = duration
        self.mode = mode
        self.user_id = User_ID
        self.id = Product.Product_ID
        Product.Product_ID += 1

    def start():
        pass

    def add_measurements():
        pass

    def end():
        pass

    class Measure:

        Measure_ID = 1

        def __init__(self, alpha, beta, gamma, delta, theta):
            self.alpha = alpha
            self.beta = beta
            self.gamma = gamma
            self.delta = delta
            self.theta = theta
            self.id = Product.Measure.Measure_ID
            Product.Measure.Measure_ID += 1

        def measure():
            pass


class Profile:

    Profile_ID = 1

    def __init__(self, measurement):
        self.measurement = measurement
        self.id = Profile.Profile_ID
        Profile.Profile_ID += 1

    def get_calculation():
        pass

    def get_measurement():
        pass

    class Calculation:

        Calculation_ID = 1

        def __init__(self):
            self.id = Profile.Calculation.Calculation_ID
            Profile.Calculation.Calculation_ID += 1

        def calculate():
            pass


# domain Project
class Project:

    Project_ID = 1

    def __init__(self, name, startdate, enddate):
        self.name = name
        self.startdate = startdate
        self.enddate = enddate
        self.id = Project.Project_ID
        Project.Project_ID += 1

    def delete_project():
        pass

    def end_project():
        pass


# domain Invoice
class Invoice:

    Invoice_ID = 1

    def __init__(self, invoicenr, date, total, due_date, Project_ID):
        self.incoicenr = invoicenr
        self.date = date
        self.total = total
        self.due_date = due_date
        self.project_id = Project_ID
        self.id = Invoice.Invoice_ID
        Invoice.Invoice_ID += 1
