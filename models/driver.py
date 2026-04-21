
class Driver:
    def __init__(self, id, name, nationality, team, skill, aggression, consistency):
        # DRIVER INFO
        # Unique identifier for driver
        self.id = id
        # Name of driver
        self.name = name
        # Nationality of driver
        self.nationality = nationality
        # Driver's team
        self.team = team
        # Driver's skill level (0-100)
        self.skill = skill
        # Driver's aggression level (0-100)
        self.aggression = aggression
        # Driver's consistency level (0-100)
        self.consistency = consistency

        # CHAMPIONSHIP
        self.points = 0

        # RACE STATE
        # Total race time so far
        self.total_time = 0.0
        # Amount of tyre wear
        self.tyre_wear = 0
        # Whether the driver has DNFed
        self.dnf = False
        # Driver's current position in the race
        self.current_position = None