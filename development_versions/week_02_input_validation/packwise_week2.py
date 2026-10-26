print("========================================")
print("                PACKWISE")
print("      A Personalised Packing Assistant")
print("========================================")

print()
print("Let's build your personalised packing list.")
print()

# TRIP DURATION
while True:
    trip_days = input(
        "How many days are you travelling for? "
    ).strip()

    if trip_days.isdigit():
        trip_days = int(trip_days)

        if trip_days > 0:
            break

    print("Please enter a valid number greater than 0.")
    print()

# DAYTIME WEATHER
day_weather = input(
    "Daytime weather "
    "(hot / warm / mild / cool / cold): "
).lower().strip()

while day_weather not in [
    "hot",
    "warm",
    "mild",
    "cool",
    "cold"
]:
    print("Please enter hot, warm, mild, cool or cold.")

    day_weather = input(
        "Daytime weather: "
    ).lower().strip()

# NIGHTTIME WEATHER
night_weather = input(
    "Nighttime weather "
    "(hot / warm / mild / cool / cold): "
).lower().strip()

while night_weather not in [
    "hot",
    "warm",
    "mild",
    "cool",
    "cold"
]:
    print("Please enter hot, warm, mild, cool or cold.")

    night_weather = input(
        "Nighttime weather: "
    ).lower().strip()

# OCCASION
occasion = input(
    "Main planned occasion "
    "(casual / beach / dinner / nightlife / formal): "
).lower().strip()

while occasion not in [
    "casual",
    "beach",
    "dinner",
    "nightlife",
    "formal"
]:
    print(
        "Please enter casual, beach, dinner, nightlife or formal."
    )

    occasion = input(
        "Main planned occasion: "
    ).lower().strip()

# WALKING LEVEL
walking_level = input(
    "Walking level "
    "(low / moderate / high): "
).lower().strip()

while walking_level not in [
    "low",
    "moderate",
    "high"
]:
    print("Please enter low, moderate or high.")

    walking_level = input(
        "Walking level: "
    ).lower().strip()

# SUMMARY
print()
print("========================================")
print("              TRIP SUMMARY")
print("========================================")
print("Trip duration:", trip_days, "days")
print("Daytime weather:", day_weather.title())
print("Nighttime weather:", night_weather.title())
print("Planned occasion:", occasion.title())
print("Walking level:", walking_level.title())
print("========================================")
