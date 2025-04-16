# planetaryweight.py

# Dictionary of planets and their gravity ratios compared to Earth
planet_gravity = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

# Prompt the user for their Earth weight
earth_weight = float(input("Enter a weight on Earth: "))

# Prompt the user for the planet name
planet = input("Enter a planet: ")

# Get the gravity ratio for the given planet
if planet in planet_gravity:
    gravity_ratio = planet_gravity[planet]
    planet_weight = round(earth_weight * gravity_ratio, 2)
    print(f"The equivalent weight on {planet}: {planet_weight}")
else:
    print("Unknown planet. Please enter a valid planet name with the first letter capitalized.")
