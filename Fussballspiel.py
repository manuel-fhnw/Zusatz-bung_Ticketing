from Ticket import Ticket
from Team import Team
from datetime import date


class Fussballspiel:
    def __init__(
        self, team_home: Team, team_away: Team, datum: date, ort: str, max_tickets: int
    ):
        self.team_home = team_home
        self.team_away = team_away
        self.datum = datum
        self.ort = ort
        self.max_tickets = max_tickets
        self.tickets = []

    def sell_tickets(self, besitzer, preis, kategorie):
        if len(self.tickets) >= self.max_tickets:
            raise ValueError("Event ist ausverkauft!")

        ticket = Ticket(besitzer, preis, kategorie)
        self.tickets.append(ticket)
        return ticket

    def free_seats(self):
        return self.max_tickets - len(self.tickets)

    def __str__(self):
        return (
            f"{self.team_home.name} vs {self.team_away.name} (Super League)/n"
            f"Datum: {self.datum}, Ort: {self.ort}/n"
            f"Tickets: {self.tickets} / {self.max_tickets}"
        )
