
class Circuit:
    def __init__(self, id, name, race, country, laps, base_lap_time, length):
        # Unique identifer for circuit
        self.id = id
        # Name of circuit
        self.name = name
        # Name of grand prix
        self.race = race
        # Name of country
        self.country = country
        # Laps of circuit
        self.laps = laps
        # Base lap time around the circuit
        self.base_lap_time = base_lap_time
        # Length of lap around the circuit (in miles)
        self.length = length