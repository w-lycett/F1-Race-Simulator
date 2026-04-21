# Import json to load .json files containing data
import json
# Import classes from relevant files
from models.driver import Driver
from models.team import Team
from models.circuit import Circuit
from models.season import Season
from simulation.championship import Championship

def load_drivers_data():
    # Open JSON file + extract driver data
    with open("data/drivers.json") as f:
        drivers_data = json.load(f)
    drivers = []
    # Create objects for each driver in the JSON file + add to list
    for d in drivers_data["drivers"]:
        drivers.append(Driver(d["id"], d["name"], d["nationality"], d["team"], d["skill"], d["aggression"], d["consistency"]))
    return drivers

def load_teams_data():
    # Open JSON file + extract team data
    with open("data/teams.json") as f:
        teams_data = json.load(f)
    teams = []
    # Create objects for each team in the JSON file + add to list
    for t in teams_data["teams"]:
        teams.append(Team(t["id"], t["name"], t["nationality"], t["car"]))
    return teams

def load_circuits_data():
    # Open JSON file + extract circuit data
    with open("data/circuits.json") as f:
        circuits_data = json.load(f)
    circuits = []
    # Create objects for each circuit in the JSON file + add to list
    for c in circuits_data["circuits"]:
        circuits.append(Circuit(c["id"], c["name"], c["race"], c["country"], c["laps"], c["base_lap_time"], c["length"]))
    return circuits

def load_seasons_data():
    # Open JSON file + extract season data
    with open("data/seasons.json") as f:
        seasons_data = json.load(f)
    seasons = []
    # Create objects for each season in the JSON file + add to list
    for s in seasons_data["seasons"]:
        seasons.append(Season(s["year"], s["calendar"], s["points_system"]))
    return seasons

def main():
    # Add all data from JSON files to lists
    drivers = load_drivers_data()
    teams = load_teams_data()
    circuits = load_circuits_data()
    seasons = load_seasons_data()

    # Replace team identifier with team object
    for driver in drivers:
        for team in teams:
            if driver.team == team.id:
                driver.team = team
                break
    
    # Replace circuit identifier with circuit object in the race calendar
    for race in seasons[0].calendar:
        for circuit in circuits:
            if race == circuit.id:
                temp = seasons[0].calendar.index(race)
                seasons[0].calendar[temp] = circuit
                break
    
    # Begin season simulation
    my_championship = Championship(seasons[0], drivers, teams)
    my_championship.run_season()

if __name__ == "__main__":
    main()