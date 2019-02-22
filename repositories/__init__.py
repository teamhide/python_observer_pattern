from subject import Subject
from observers import Observer


class Repository(Observer):
    def __init__(self, subject: Subject):
        self.subject = subject

    def save_user(self):
        try:
            raise Exception()
            print("[*] Repository START")
            print(self.subject.state)
            print("[*] Repository STOP")
        except Exception:
            print("[*] Repository Exception")
            self.subject.notify_all()
