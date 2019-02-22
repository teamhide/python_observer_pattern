from typing import Type
from repositories import Repository
from observers import Observer


class Interactor(Observer):
    def __init__(self, subject: 'Subject'):
        self.subject = subject
        self.subject.register(self)
        self.repository = Repository(self.subject)

    def execute(self):
        try:
            print("[*] Interactor START")
            file1 = '1.jpg'
            file2 = '2.jpg'
            self.subject.state.extend([file1, file2])
            self.repository.save_user()
            print("[*] Interactor STOP")

        except Exception:
            print("[*] Interactor Exception")
            self.subject.notify_all()
