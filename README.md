# F1-Race-Simulator
A lightweight, text-based motorsport simulator for F1 races. Focuses on customisability by letting users choose their own drivers, teams and circuits. Can easily be applied to similar motorsport series, real or fictional.

## Overview
I started creating a race simulator after finding no similar alternative that I could use for recreational purposes. I specifically wanted to introduce functionality that allows for almost all aspects to be customised, especially the drivers and teams. This allows it to be flexibly applied to any racing series that uses a similar race format. While the customisation ability limits the simulation algorithm somewhat, I decided this was a necessary sacrifice, with multiple editable attributes for teams and drivers to compensate.

## Features
- Simulate F1 race conditions with pit stops, fastest laps and DNFs.
- Customise drivers, teams, circuits and seasons.
- Console-based output, with GUI functionality planned for the future.

## Requirements
- Python 3.13+
- (Optional) Virtual environment tool (venv)
- OS: Windows / macOS / Linux

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/w-lycett/F1-Race-Simulator.git
   cd F1-Race-Simulator
   ```

3. (Recommended) Create a virtual environment:
   ```
   python -m venv venv
   ```

5. Activate the virtual environment:
   Windows:
     ```
     venv\Scripts\activate
     ```
   macOS / Linux:
     ```
     source venv/bin/activate
     ```

7. Run the simulator from the project root:
   ```
   python -m main
   ```
   The race simulation should start in the console.

## Customisation
To customise the drivers, teams, etc., edit the parameters in the JSON files. Rest assured a more graceful solution will be implemented alongside the GUI. Use the following formats:
Drivers:
  ```
  "id": <string> [driver's unique identifier]
  "name": <string> [driver's display name]
  "nationality": <string> [driver's country]
  "team": <string> [unique identifier for the driver's team]
  "skill": <integer> [skill score (0-100)]
  "aggression": <integer> [aggression score (0-100)]
  "consistency": <integer> [consistency score (0-100)]
  ```
Teams:
  ```
  "id": <string> [team's unique identifier (usually the chassis prefix)]
  "name": <string> [team's display name]
  "nationality": <string> [team's country]
  "car": <integer> [car power / reliability score (0-100)]
  ```
Circuits:
  ```
  "id": <string> [circuit's unique identifier]
  "circuit": <string> [circuit's full display name]
  "race": <string> [grand prix name]
  "country": <string> [country of the circuit]
  "laps": <integer> [number of laps of the circuit]
  "base_lap_time": <float> [average lap time around the circuit, in seconds]
  "length": <float> [length of a lap around the circuit, in miles]
  ```
Seasons:
  ```
  "year": <integer> [year of the season]
  "calendar": <string array> [circuits in the season, using unique identifiers]
  "points_system": <integer array> [points awarded, in decreasing order of positions]
  ```
Currently, program only simulates the first season in the JSON file. Functionality to choose seasons will be implemented alongside the GUI.

## Contributing
Pull requests are welcome. For major changes, open an issue first.

## License
MIT License
