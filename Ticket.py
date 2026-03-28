from Person import Person
import uuid


class Ticket:
    def __init__(self, besitzer: Person, preis: float, kategorie: str):
        self.ticket_id = uuid.uuid4()
        self.besitzer = besitzer
        self.preis = preis
        self.kategorie = kategorie

    def __str__(self):
        return f"Ticket #{self.ticket_id} - {self.kategorie} - {self.preis} CHF - Besitzer: {self.besitzer}"
