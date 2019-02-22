from subject import Subject
from interactors import Interactor


class View:
    def __init__(self):
        self.subject = Subject()

    def view(self):
        print("[*] VIEW START")
        Interactor(self.subject).execute()
        print("[*] VIEW END")
