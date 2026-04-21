
class Season:
    def __init__(self, year, calendar, points_system):
        # Year of the season
        self.year = year
        # Circuits that make up the race calendar
        self.calendar = calendar
        # How many points the top drivers get
        self.points_system = points_system