# domain User
class User:

    userId = 1

    def __init__(self, name, email, password, date_of_birth, gender, profileId):
        self.name = name
        self.email = email
        self.password = password
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.profileId = profileId
        self.id = User.userId
        User.userId += 1

    def reset_password(self, reset_password):
        self.password = reset_password

    def logIn(self, username, password):
        self.username = username
        self.password = password
        pass

    def storeUserInDB(self):
        pass


    class Subscription:

        subscriptionId = 1

        def __init__(self, subscription=True):
            self.subscription = subscription
            self.userId = User.userId
            self.id = User.Subscription.subscriptionId
            User.Subscription.subscriptionId += 1

        def deleteSubscription(self):
            pass

        def storeSubscriptionInDB(self):
            pass

# domain Assesment
class Session:

    sessionId = 1

    def __init__(self, profileId, mode, date, time):
        self.profileId = profileId
        self.mode = mode
        self.date = date
        self.time = time
        self.id = Session.sessionId
        Session.sessionId += 1

    def deleteSession(self):
        pass

    def convertToCSV(self):
            pass

    class Profile:

        profileId = 1

        def __innit__(self):
            self.id = Session.Profile.profileId
            Session.Profile.profileId += 1

    class SessionFactory:

        sessionFactoryId = 1

        def __init__(self, sessionId, lowAlpha, highAlpha, lowBeta, highBeta, theta, lowGamma, middleGamma, delta):
            self.sessionId = sessionId
            self.lowAlpha = lowAlpha
            self.highAlpha = highAlpha
            self.lowBeta = lowBeta
            self.highBeta = highBeta
            self.theta = theta
            self.lowGamma = lowGamma
            self.middleGamma = middleGamma
            self.delta = delta
            self.id = Session.SessionFactory.sessionFactoryId
            Session.SessionFactory.sessionFactoryId += 1

        def decodeSignal(self):
            pass
        
        def createCSVFile(self):
            pass

        def storeSessionInDB(self):
            pass

    class Game:

        gameId = 1

        def __innit__(self, profileId, date, time):
            self.profileId = profileId
            self.date = date
            self.time = time
            self.id = Session.Game.gameId
            Session.Game.gameId += 1

# domain Dashboard
class Dashboard:

    dashboardId = 1

    def __init__(self, CogLoad, Flow, Focus, Stress, Alpha, Beta, Gamma):
        self.CogLoad = CogLoad
        self.Flow = Flow
        self.Focus = Focus
        self.Stress = Stress
        self.Alpha = Alpha
        self.Beta = Beta
        self.Gamma = Gamma
        self.id = Dashboard.dashboardId
        Dashboard.dashboardId += 1

    def calculatePerformance(self):
        pass

    def visualize(self):
        pass

    def createReport(self):
        pass

    class DashboardFactory:

        dashboardFactoryId = 1

        def __init__(self, profileId, performance, activity):
            self.profileId = profileId
            self.performance = performance
            self.activity = activity
            self.id = Dashboard.DashboardFactory.dashboardFactoryId
            Dashboard.DashboardFactory.dashboardFactoryId += 1

        def decodeSignal(self):
            pass

        def createCSVFile(self):
            pass

        def storeSessionInDB(self):
            pass

# domain Training
class Meditation:

    meditationId = 1

    def __init__(self, profileId, date, time):
        self.profileId = profileId
        self.date = date
        self.time = time
        self.id = Meditation.meditationId
        Meditation.meditationId += 1

    def storeMeditationInDB(self):
            pass

    def getMeditation(self):
        pass

    def getRecommendation(self):
        pass

    def getMeditationHistory(self):
        pass

