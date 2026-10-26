print("========================================")
print("                PACKWISE")
print("      A Personalised Packing Assistant")
print("========================================")
print()

# TRIP LENGTH
while True:
    trip_days_input = input(
        "How many days are you travelling for? "
    ).strip()

    if trip_days_input.isdigit():
        trip_days = int(trip_days_input)

        if trip_days > 0:
            break

    print("Please enter a valid number greater than 0.")

# WEATHER
valid_weather = [
    "hot",
    "warm",
    "mild",
    "cool",
    "cold"
]

day_weather = input(
    "Daytime weather "
    "(hot / warm / mild / cool / cold): "
).lower().strip()

while day_weather not in valid_weather:
    print("Invalid weather option.")

    day_weather = input(
        "Daytime weather: "
    ).lower().strip()

night_weather = input(
    "Nighttime weather "
    "(hot / warm / mild / cool / cold): "
).lower().strip()

while night_weather not in valid_weather:
    print("Invalid weather option.")

    night_weather = input(
        "Nighttime weather: "
    ).lower().strip()

# MULTIPLE OCCASIONS
valid_occasions = [
    "casual",
    "beach",
    "dinner",
    "nightlife",
    "formal"
]

while True:
    occasion_input = input(
        "Enter your planned occasions separated by commas\n"
        "(casual / beach / dinner / nightlife / formal): "
    ).lower()

    occasions = occasion_input.split(",")

    clean_occasions = []
    invalid_found = False

    for occasion in occasions:
        occasion = occasion.strip()

        if occasion in valid_occasions:
            if occasion not in clean_occasions:
                clean_occasions.append(occasion)
        else:
            invalid_found = True

    if invalid_found == False and len(clean_occasions) > 0:
        break

    print()
    print("One or more occasions were invalid.")
    print("Please try again.")
    print()

# WALKING
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
        "Walking level: "
    ).lower().strip()

# CALCULATE GENERAL QUANTITIES
top_quantity = max(
    2,
    (trip_days + 1) // 2
)

bottom_quantity = max(
    1,
    (trip_days + 2) // 3
)

underwear_quantity = trip_days
sock_quantity = trip_days

sleepwear_quantity = max(
    1,
    (trip_days + 4) // 5
)

# CREATE PACKING LISTS
tops = []
bottoms = []
layers = []
outerwear = []
footwear = []
extras = []

# DAY WEATHER
if day_weather == "hot":
    tops.append(
        str(top_quantity) +
        " lightweight breathable tops"
    )
    bottoms.append(
        str(bottom_quantity) +
        " shorts or lightweight bottoms"
    )
    extras.append("Sunglasses")

elif day_weather == "warm":
    tops.append(
        str(top_quantity) +
        " T-shirts or lightweight tops"
    )
    bottoms.append(
        str(bottom_quantity) +
        " lightweight bottoms"
    )

elif day_weather == "mild":
    tops.append(
        str(top_quantity) +
        " everyday tops"
    )
    bottoms.append(
        str(bottom_quantity) +
        " jeans or trousers"
    )
    layers.append("1 light jumper")

elif day_weather == "cool":
    tops.append(
        str(top_quantity) +
        " long-sleeve tops"
    )
    bottoms.append(
        str(bottom_quantity) +
        " long pants"
    )
    layers.append("1-2 warm jumpers")
    outerwear.append("1 light jacket")

else:
    tops.append(
        str(top_quantity) +
        " warm or thermal tops"
    )
    bottoms.append(
        str(bottom_quantity) +
        " warm trousers"
    )
    layers.append("2 warm layers")
    outerwear.append("1 insulated coat")

# NIGHT WEATHER
if night_weather == "warm":
    layers.append("1 lightweight evening layer")

elif night_weather == "mild":
    layers.append("1 cardigan or light jumper")

elif night_weather == "cool":
    layers.append("1 warm evening jumper")
    outerwear.append("1 evening jacket")

elif night_weather == "cold":
    layers.append("1 heavy evening layer")
    outerwear.append("1 warm coat")

# OCCASIONS
for occasion in clean_occasions:
    if occasion == "casual":
        tops.append("1 versatile casual top")

    elif occasion == "beach":
        extras.append("1-2 sets of swimwear")
        extras.append("1 beach cover-up")
        footwear.append("1 pair sandals or slides")

    elif occasion == "dinner":
        tops.append("1 smart evening top")
        bottoms.append("1 smart evening bottom")
        footwear.append("1 pair dinner shoes")

    elif occasion == "nightlife":
        tops.append("1 going-out top")
        bottoms.append("1 evening bottom")
        footwear.append("1 pair going-out shoes")

    elif occasion == "formal":
        extras.append("1 formal outfit")
        footwear.append("1 pair formal shoes")

# WALKING
if walking_level == "high":
    footwear.append("1 pair supportive walking shoes")

    if trip_days >= 7:
        footwear.append("1 backup pair comfortable shoes")

elif walking_level == "moderate":
    footwear.append("1 pair comfortable sneakers")

else:
    footwear.append("1 pair everyday shoes")

# ESSENTIALS
extras.append(
    str(underwear_quantity) +
    " pairs of underwear"
)

extras.append(
    str(sock_quantity) +
    " pairs of socks"
)

extras.append(
    str(sleepwear_quantity) +
    " sets of sleepwear"
)

# REMOVE DUPLICATES
tops = list(dict.fromkeys(tops))
bottoms = list(dict.fromkeys(bottoms))
layers = list(dict.fromkeys(layers))
outerwear = list(dict.fromkeys(outerwear))
footwear = list(dict.fromkeys(footwear))
extras = list(dict.fromkeys(extras))

# DISPLAY SUMMARY
print()
print("========================================")
print("              TRIP SUMMARY")
print("========================================")
print("Duration:", trip_days, "days")
print("Day weather:", day_weather.title())
print("Night weather:", night_weather.title())
print(
    "Occasions:",
    ", ".join(clean_occasions).title()
)
print("Walking:", walking_level.title())

# DISPLAY LIST
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
if len(layers) == 0:
    print("- No additional layers required")
else:
    for item in layers:
        print("-", item)

print()
print("OUTERWEAR")
if len(outerwear) == 0:
    print("- No heavy outerwear required")
else:
    for item in outerwear:
        print("-", item)

print()
print("FOOTWEAR")
for item in footwear:
    print("-", item)

print()
print("EXTRAS + ESSENTIALS")
for item in extras:
    print("-", item)

print()
print("========================================")
print("Pack smarter, not heavier.")
print("========================================")
