print("========================================")
print("                PACKWISE")
print("      A Personalised Packing Assistant")
print("========================================")
print()

# GET TRIP LENGTH
while True:
    trip_days = input(
        "How many days are you travelling for? "
    ).strip()

    if trip_days.isdigit():
        trip_days = int(trip_days)

        if trip_days > 0:
            break

    print("Please enter a number greater than 0.")

# DAY WEATHER
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
    print("Invalid weather option.")

    day_weather = input(
        "Please enter hot, warm, mild, cool or cold: "
    ).lower().strip()

# NIGHT WEATHER
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
    print("Invalid weather option.")

    night_weather = input(
        "Please enter hot, warm, mild, cool or cold: "
    ).lower().strip()

# OCCASION
occasion = input(
    "Main occasion "
    "(casual / beach / dinner / nightlife / formal): "
).lower().strip()

while occasion not in [
    "casual",
    "beach",
    "dinner",
    "nightlife",
    "formal"
]:
    print("Invalid occasion.")

    occasion = input(
        "Please enter casual, beach, dinner, nightlife or formal: "
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
    print("Invalid walking level.")

    walking_level = input(
        "Please enter low, moderate or high: "
    ).lower().strip()

# CREATE EMPTY PACKING CATEGORIES
tops = []
bottoms = []
layers = []
outerwear = []
footwear = []
extras = []

# DAYTIME WEATHER RULES
if day_weather == "hot":
    tops.append("Lightweight breathable tops")
    bottoms.append("Shorts or lightweight bottoms")
    extras.append("Sunglasses")

elif day_weather == "warm":
    tops.append("T-shirts or lightweight tops")
    bottoms.append("Lightweight pants or shorts")

elif day_weather == "mild":
    tops.append("T-shirts")
    tops.append("Long-sleeve top")
    bottoms.append("Jeans or lightweight trousers")
    layers.append("Light jumper")

elif day_weather == "cool":
    tops.append("Long-sleeve tops")
    bottoms.append("Long pants")
    layers.append("Warm jumper")
    outerwear.append("Light jacket")

else:
    tops.append("Thermal or warm tops")
    tops.append("Long-sleeve tops")
    bottoms.append("Warm trousers")
    layers.append("Warm knitwear")
    outerwear.append("Insulated coat")

# NIGHTTIME WEATHER RULES
if night_weather == "hot":
    tops.append("Light evening top")

elif night_weather == "warm":
    layers.append("Light evening layer")

elif night_weather == "mild":
    layers.append("Cardigan or light jumper")

elif night_weather == "cool":
    layers.append("Warm evening jumper")
    outerwear.append("Light evening jacket")

else:
    layers.append("Heavy warm layer")
    outerwear.append("Warm coat")

# OCCASION RULES
if occasion == "casual":
    tops.append("Casual everyday top")
    bottoms.append("Comfortable casual bottoms")

elif occasion == "beach":
    extras.append("Swimwear")
    footwear.append("Sandals or slides")
    extras.append("Beach cover-up")

elif occasion == "dinner":
    tops.append("Smart evening top")
    bottoms.append("Smart pants or skirt")
    footwear.append("Dinner shoes")

elif occasion == "nightlife":
    tops.append("Going-out top")
    bottoms.append("Evening bottoms")
    footwear.append("Going-out shoes")

else:
    extras.append("Formal outfit")
    footwear.append("Formal shoes")

# WALKING RULES
if walking_level == "high":
    footwear.append("Comfortable walking shoes")

elif walking_level == "moderate":
    footwear.append("Comfortable sneakers")

else:
    footwear.append("Everyday shoes")

# DISPLAY RESULTS
print()
print("========================================")
print("          YOUR PACKWISE LIST")
print("========================================")

print()
print("TOPS")
for item in tops:
    print("-", item)

print()
print("BOTTOMS")
for item in bottoms:
    print("-", item)

print()
print("LAYERS")
for item in layers:
    print("-", item)

print()
print("OUTERWEAR")
for item in outerwear:
    print("-", item)

print()
print("FOOTWEAR")
for item in footwear:
    print("-", item)

print()
print("EXTRAS")
for item in extras:
    print("-", item)

print()
print("========================================")
print("PackWise complete.")
print("========================================")
