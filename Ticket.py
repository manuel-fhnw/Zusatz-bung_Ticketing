import Kunden
import uuid


class Ticket(Kunden):
    def __init__(self, ticket_id: int, besitzer: Kunden, preis: float, kategorie: str):
        self.besitzer = besitzer
        self.ticket_id = uuid.uuid5()
        self.preis = preis
        self.kategorie = kategorie

    def __str__(self):
        return f"Ticket #{self.ticket_id} - {self.kategorie} - {self.preis} CHF - Besitzer: {self.besitzer}"
