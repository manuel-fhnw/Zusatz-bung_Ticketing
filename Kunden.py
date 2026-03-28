class Kunde:
    def __init__(self, vorname, nachname, mail):
        self.vorname = vorname
        self.nachname = nachname
        self.mail = mail

    def __str__(self):
        return f"{self.vorname} {self.nachname} ({self.mail})"
