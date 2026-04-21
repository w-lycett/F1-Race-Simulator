
class Team:
    def __init__(self, id, name, nationality, car):
        # TEAM INFO
        # Unique identifier for team
        self.id = id
        # Name of team
        self.name = name
        # Nationality of team
        self.nationality = nationality
        # Car power level (0-100)
        self.car = car

        # CHAMPIONSHIP
        self.points = 0