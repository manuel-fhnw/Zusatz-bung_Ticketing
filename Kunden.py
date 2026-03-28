class Kunde:
    def __init__(self, vorname: str, nachname: str, mail: str):
        if "@" not in mail:
            raise ValueError("Ungültige E-Mail-Adresse")

        self.vorname = vorname
        self.nachname = nachname
        self.mail = mail

    @property
    def name(self):
        return f"{self.vorname} {self.nachname}"

    def __str__(self):
        return f"{self.name} ({self.mail})"

    def __eq__(self, other):
        return isinstance(other, Kunde) and self.mail == other.mail

    def __hash__(self):
        return hash(self.mail)
