# Import random for variation in lap times
import random
# Import console class to output results
from simulation.console import Console

class RaceEngine:
    def __init__(self, circuit, drivers):
        # Circuit object
        self.circuit = circuit
        # Driver objects
        self.drivers = drivers
        # Current lap
        self.lap = 0
        # Fastest lap time
        self.fastest_lap = float("inf")
        # Driver who set fastest lap time
        self.fastest_driver = None
    
    def simulate_race(self):
        # Initialise the race by resetting every driver's state
        for driver in self.drivers:
            driver.total_time = 0.0
            driver.tyre_wear = 0
            driver.dnf = False
            driver.current_position = None
        
        # Start message
        Console.print_start(self.circuit)
        
        # Begin the race simulation lap-by-lap
        for lap in range(1, self.circuit.laps + 1):
            self.lap = lap
            self.simulate_lap()
        return self.get_results()

    def simulate_lap(self):
        # Advance each driver if not DNFed
        for driver in self.drivers:
            if driver.dnf:
                continue
            # Calculate their lap time + add it to their total race time
            lap_time = self.calculate_lap_time(driver)
            driver.total_time += lap_time
            # Check for fastest driver
            self.update_fastest_lap(driver, lap_time)
            # Add time deficit if driver pitted
            if not self.check_pit_stop(driver):
                # Update driver state if DNFed (provided they didn't pit that lap)
                self.check_dnf(driver)
        # Update the list storing driver positions
        self.update_positions()
    
    def calculate_lap_time(self, driver):
        base = self.circuit.base_lap_time
        # Calculates skill bonus to lap time
        skill_bonus = driver.skill * 0.02
        # Calculates car power bonus to lap time
        car_bonus = driver.team.car * 0.02
        # Calculates how much time lost to tyre wear
        tyre_penalty = driver.tyre_wear * 0.05
        # Calculates aggression bonus to lapt time
        aggression_bonus = driver.aggression * 0.01

        # Calculates randomness based on driver consistency (less consistent = more variation)
        consistency_factor = (100 - driver.consistency) / 100
        random_range = 0.3 + (consistency_factor * 0.7)
        randomness = random.uniform(-random_range, random_range)

        # Apply bonuses + costs to calculate current lap time
        lap_time = base - skill_bonus - car_bonus - aggression_bonus + tyre_penalty + randomness
        
        # Calculate the chance to make a small mistake that costs some lap time
        mistake_chance = ((100 - driver.consistency) * 0.0005 + driver.aggression * 0.0003)
        if random.random() < mistake_chance:
            mistake_time = random.uniform(1, 3)
            lap_time += mistake_time

        # Increase tyre wear
        self.increase_tyre_wear(driver)

        # Return rounded lap time
        return round(lap_time, 3)

    def increase_tyre_wear(self, driver):
        # Base wear per mile
        base_wear_per_mile = 0.7
        # Create a base for tyre wear
        variation = random.uniform(-0.2, 0.2)
        # Increase tyre wear based on aggression
        aggression_multiplier = 1 + (driver.aggression / 100) * 0.5
        # Combine factors to calculate total tyre wear
        driver.tyre_wear += (base_wear_per_mile + variation) * self.circuit.length * aggression_multiplier
    
    def update_fastest_lap(self, driver, lap_time):
        if lap_time < self.fastest_lap:
            # Update attributes to store fastest lap time + driver who set it
            self.fastest_lap = lap_time
            self.fastest_driver = driver
            Console.print_fastest_lap(driver.name, lap_time, self.lap)
    
    def check_pit_stop(self, driver):
        # Driver pits if tyre wear is too great
        if driver.tyre_wear > 70:
            # Add time cost to total time
            pit_loss = 20
            driver.total_time += pit_loss
            # Reset tyre wear
            driver.tyre_wear = 0
            Console.print_pit_stop(driver.name, self.lap)
            return True
        return False
    
    def check_dnf(self, driver):
        # Stop if already DNFed
        if driver.dnf:
            return
        # Calculates DNF risk based on car power + driver aggression
        reliability = driver.team.car
        aggression_risk = driver.aggression * 0.00005

        # Calculates DNF risk based on high tyre wear
        tyre_risk = 0
        if driver.tyre_wear > 70:
            tyre_risk = (driver.tyre_wear - 70) * 0.0005

        # Combine all risks to calculate chance to DNF
        chance = 0.0005 + aggression_risk + tyre_risk + (100 - reliability) * 0.00001
        if random.random() < chance:
            driver.dnf = True
            Console.print_DNF(driver.name, self.lap)
    
    def update_positions(self):
        # Sort the list of drivers based on total race time so far
        self.drivers.sort(key = lambda d: (d.dnf, d.total_time))
        for i, driver in enumerate(self.drivers):
            # Update driver position attributes
            driver.current_position = i + 1
    
    def get_results(self):
        # Create list of drivers who finished the race
        classified = [d for d in self.drivers if not d.dnf]
        # Create list of drivers who didn't finish the race
        dnfs = [d for d in self.drivers if d.dnf]

        # Output race results
        Console.print_race_results(classified, dnfs)

        # Add DNFed drivers to rear of list
        results = classified + dnfs
        return results