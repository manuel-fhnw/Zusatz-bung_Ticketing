from datetime import date
from Person import Person
from Team import Team
from Fussballspiel import Fussballspiel
from TicketSystem import TicketSystem

print("=== TEST: Ticketing-System ===\n")

# --- Teams ---
basel = Team("FC Basel", "Basel", date(1893, 11, 15))
zuerich = Team("FC Zürich", "Zürich", date(1896, 8, 1))

print("Teams erstellt:")
print(basel)
print(zuerich)
print()

# --- Personen ---
manuel = Person("Manuel", "Muster", "manuel@example.com")
anna = Person("Anna", "Meier", "anna@example.com")
print("Personen erstellt:")
print(manuel)
print(anna)
print()

# --- Event ---
spiel = Fussballspiel(
    team_home=basel,
    team_away=zuerich,
    datum=date(2026, 5, 12),
    ort="St. Jakob-Park",
    max_tickets=3,
)

print("Event erstellt:")
print(spiel)
print()

# --- TicketSystem ---
system = TicketSystem()
system.add_event(spiel)

# --- Tickets verkaufen ---
print("Tickets werden verkauft...\n")

system.sell("FC Basel vs FC Zürich", manuel, 120, "VIP")
system.sell("FC Basel vs FC Zürich", anna, 80, "Stehplatz")

print("Event nach Verkäufen:")
print(spiel)
print()

# --- Freie Plätze ---
print(f"Freie Plätze: {spiel.free_seats()}\n")

# --- Fehlerfall: ausverkauft ---
try:
    system.sell("FC Basel vs FC Zürich", manuel, 100, "Sitzplatz")
    system.sell("FC Basel vs FC Zürich", anna, 100, "Sitzplatz")  # sollte Fehler werfen
except ValueError as e:
    print("Erwarteter Fehler:", e)
print()

# --- Report ---
print("=== REPORT ===")
system.report(sort_by="auslastung")
