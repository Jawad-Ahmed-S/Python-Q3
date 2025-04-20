
Weights = {
    "mercury": 37.6,
    "venus": 88.9,
    "mars": 37.8,
    "jupiter": 236.0,
    "saturn": 108.1,
    "uranus": 81.5,
    "neptune": 114.0
}

weight = int(input("Enter your weight on Earth: "))
planet = input("Enter the name of the planet: ")
planet = planet.lower();

def Weight_On_Planet(weight,planet):
    if planet in Weights:
        weight_on_planet = weight * Weights[planet] / 100
        return weight_on_planet
    else:
        return "Invalid planet name"

print(Weight_On_Planet(weight,planet));