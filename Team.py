from datetime import date


class Team:
    def __init__(self, name: str, stadt: str, gruendungsjahr: date.year):
        self.name = name
        self.stadt = stadt
        self.gruendungsjahr = gruendungsjahr


def __str__(self):
    return f"{self.name} ({self.stadt}), gegründet im Jahr: {self.gruendungsjahr}"
