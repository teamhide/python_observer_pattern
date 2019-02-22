class Subject:
    def __init__(self):
        self.observers = []
        self.state = []

    def register(self, observer):
        self.observers.append(observer)

    def notify_all(self):
        for observer in self.observers:
            observer.notify(self)
