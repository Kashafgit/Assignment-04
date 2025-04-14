# Milestone 1

# earth_weight = float(input("Enter a weight on earth: "))
# mars_gravity = 0.378
# mars_weight = earth_weight * mars_gravity
# print("The equivalent on mars", mars_weight)

# Milestone 2

planet_gravity = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}
earth_weight = float(input("Enter a weight on earth: "))
planet = input("Enter a planet: ")
if planet in planet_gravity:
    wight_on_earth = earth_weight * planet_gravity[planet]
    print(f"The equivalent of {planet} is {wight_on_earth}")
else:
    print("Invlid planet")