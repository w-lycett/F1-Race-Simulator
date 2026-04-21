# Import classes from relevant files
from simulation.race import RaceEngine
from simulation.console import Console

class Championship:
    def __init__(self, season, drivers, teams):
        # Season object
        self.season = season
        # Driver objects
        self.drivers = drivers
        # Team objects
        self.teams = teams

        # All circuits in the season
        self.circuits = season.calendar
        # Points system to be used in the season
        self.points_system = self.season.points_system
        # Current race of the season
        self.current_round = 0
    
    def run_season(self):
        # Initialise the championship by resetting every driver's points
        for driver in self.drivers:
            driver.points = 0

        # Output message for season start
        Console.print_season_start(self.season)
        
        # Begin the championship simulation
        for circuit in self.circuits:
            # Run race and award points to drivers
            results = self.run_race(circuit)
            self.award_points(results)
            self.current_round += 1
            
            # Output championship standings + prompt to continue
            Console.print_WDC_standings(self.get_driver_standings())
            Console.print_WCC_standings(self.get_team_standings())
            Console.check_for_end(circuit, self.circuits, self.get_driver_standings()[0], self.get_team_standings()[0], self.season)
    
    def run_race(self, circuit):
        # Create race object for the current round of the season
        engine = RaceEngine(circuit, self.drivers)
        # Simulate the race object
        results = engine.simulate_race()
        return results
    
    def award_points(self, results):
        for i, driver in enumerate(results):
            # Award only if within the points and not DNFed
            if i < len(self.points_system) and not (driver.dnf):
                # Add points to driver + team
                driver.points += self.points_system[i]
                driver.team.points += self.points_system[i]
    
    def get_driver_standings(self):
        # Sort the drivers standings by points
        return sorted(self.drivers, key = lambda d: d.points, reverse = True)
    
    def get_team_standings(self):
        # Sort the constructors standings by points
        return sorted(self.teams, key = lambda t: t.points, reverse = True)