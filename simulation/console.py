
class Console:
    # WDC standings
    def print_WDC_standings(standings):
        input("Press enter to continue.")
        print("\n=== DRIVER STANDINGS ===")
        for driver in standings:
            print(f"{driver.name} - {driver.points} points.")
    
    # WCC standings
    def print_WCC_standings(standings):
        input("Press enter to continue.")
        print("\n=== CONSTRUCTOR STANDINGS ===")
        for team in standings:
            print(f"{team.name} - {team.points} points.")
    
    # Message for start of season
    def print_season_start(season):
        print("=== SEASON START ===")
        print(f"{season.year} Season")
        print("Races:")
        for race in season.calendar:
            print(f" - {race.race}")
        input("Press enter to continue.")

    # Message for start of a race
    def print_start(circuit):
        print("\n=== NEXT RACE ===")
        print(f"{circuit.race} - {circuit.name}")
        print(f"{circuit.country}")
        print(f"Laps - {circuit.laps}")
        print(f"Length - {circuit.length} miles")
        input("Press enter to continue.")
        print("\n=== RACE START ===")
    
    # Message for new fastest lap
    def print_fastest_lap(name, time, lap):
        print(f"{name} sets a new fastest lap of {time} on lap {lap}.")
    
    # Message for a pit stop
    def print_pit_stop(name, lap):
        print(f"{name} pits on lap {lap}.")

    # Message for DNF
    def print_DNF(name, lap):
        print(f"{name} DNFs on lap {lap}.")
    
    # Message for race results
    def print_race_results(classified, dnfs):
        print("=== RACE END ===")
        input("Press enter to continue.")
        print("\n=== RACE RESULTS ===")
        for driver in classified:
            print(f"{classified.index(driver) + 1} - {driver.name}")
        for driver in dnfs:
            print(f"DNF - {driver.name}")
    
    # Message for end of season (if reached)
    def check_for_end(circuit, circuits, drivers, teams, season):
        if circuit == circuits[-1]:
            print("\n=== SEASON END ===")
            print(f"{drivers.name} is the world champion of the {season.year} season!")
            print(f"{teams.name} are the world champion constructors of the {season.year} season!")
        else:
            input("Press enter to continue.")