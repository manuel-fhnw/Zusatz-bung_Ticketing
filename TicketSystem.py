from Fussballspiel import Fussballspiel


class TicketSystem:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def search(self, title: str):
        for event in self.events:
            event_title = f"{event.team_home.name} vs {event.team_away.name}"
            if event_title.lower() == title.lower():
                return event
        return None

    def sell(self, title, besitzer, preis, kategorie):
        event = self.search(title)
        if event is None:
            raise ValueError("Event nicht gefunden!")

        return event.sell_tickets(besitzer, preis, kategorie)

    def report(self, sort_by="datum"):
        if sort_by == "datum":
            events_sorted = sorted(self.events, key=lambda e: e.datum)
        elif sort_by == "auslastung":
            events_sorted = sorted(
                self.events, key=lambda e: len(e.tickets) / e.max_tickets, reverse=True
            )
        else:
            raise ValueError("sort_by muss 'datum' oder 'auslastung' sein.")

        print("=== TicketSystem Report ===")
        for event in events_sorted:
            auslastung = len(event.tickets) / event.max_tickets * 100
            print(
                f"{event.team_home.name} vs {event.team_away.name}"
                f"am {event.datum} - Auslastung: {auslastung:.1f}%"
            )
