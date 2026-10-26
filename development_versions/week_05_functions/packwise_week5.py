def get_trip_days():
    while True:
        answer = input(
            "How many days are you travelling for? "
        ).strip()

        if answer.isdigit():
            days = int(answer)

            if days > 0:
                return days

        print("Please enter a valid number greater than 0.")


def get_choice(question, valid_choices):
    answer = input(question).lower().strip()

    while answer not in valid_choices:
        print(
            "Please choose from:",
            ", ".join(valid_choices)
        )

        answer = input(question).lower().strip()

    return answer


def get_occasions():
    valid_occasions = [
        "casual",
        "beach",
        "dinner",
        "nightlife",
        "formal"
    ]

    while True:
        answer = input(
            "Enter planned occasions separated by commas\n"
            "(casual / beach / dinner / nightlife / formal): "
        ).lower()

        raw_occasions = answer.split(",")

        occasions = []
        invalid = False

        for occasion in raw_occasions:
            occasion = occasion.strip()

            if occasion in valid_occasions:
                if occasion not in occasions:
                    occasions.append(occasion)
            else:
                invalid = True

        if invalid == False and len(occasions) > 0:
            return occasions

        print(
            "Please enter only the available occasion options."
        )


def calculate_quantities(days):
    tops = max(2, (days + 1) // 2)
    bottoms = max(1, (days + 2) // 3)
    underwear = days
    socks = days
    sleepwear = max(1, (days + 4) // 5)

    return (
        tops,
        bottoms,
        underwear,
        socks,
        sleepwear
    )


def add_day_weather_items(
    weather,
    top_quantity,
    bottom_quantity,
    tops,
    bottoms,
    layers,
    outerwear,
    extras
):
    if weather == "hot":
        tops.append(
            str(top_quantity) +
            " lightweight breathable tops"
        )
        bottoms.append(
            str(bottom_quantity) +
            " shorts or lightweight bottoms"
        )
        extras.append("Sunglasses")

    elif weather == "warm":
        tops.append(
            str(top_quantity) +
            " lightweight tops"
        )
        bottoms.append(
            str(bottom_quantity) +
            " lightweight bottoms"
        )

    elif weather == "mild":
        tops.append(
            str(top_quantity) +
            " everyday tops"
        )
        bottoms.append(
            str(bottom_quantity) +
            " jeans or trousers"
        )
        layers.append("1 light jumper")

    elif weather == "cool":
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
            " thermal or warm tops"
        )
        bottoms.append(
            str(bottom_quantity) +
            " warm trousers"
        )
        layers.append("2 warm layers")
        outerwear.append("1 insulated coat")


def add_night_weather_items(
    weather,
    layers,
    outerwear
):
    if weather == "warm":
        layers.append("1 light evening layer")

    elif weather == "mild":
        layers.append("1 cardigan or light jumper")

    elif weather == "cool":
        layers.append("1 warm evening jumper")
        outerwear.append("1 evening jacket")

    elif weather == "cold":
        layers.append("1 heavy evening layer")
        outerwear.append("1 warm coat")


def add_occasion_items(
    occasions,
    tops,
    bottoms,
    footwear,
    extras
):
    for occasion in occasions:
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


def add_walking_items(
    walking_level,
    trip_days,
    footwear
):
    if walking_level == "high":
        footwear.append("1 pair supportive walking shoes")

        if trip_days >= 7:
            footwear.append(
                "1 backup pair comfortable shoes"
            )

    elif walking_level == "moderate":
        footwear.append("1 pair comfortable sneakers")

    else:
        footwear.append("1 pair everyday shoes")


def remove_duplicates(items):
    unique_items = []

    for item in items:
        if item not in unique_items:
            unique_items.append(item)

    return unique_items


def print_category(
    heading,
    items,
    empty_message
):
    print()
    print(heading)

    if len(items) == 0:
        print("-", empty_message)
    else:
        for item in items:
            print("-", item)


def main():
    print("========================================")
    print("                PACKWISE")
    print("      A Personalised Packing Assistant")
    print("========================================")
    print()
    print(
        "Tell PackWise about your trip and it will "
        "build a personalised packing list."
    )
    print()

    weather_options = [
        "hot",
        "warm",
        "mild",
        "cool",
        "cold"
    ]

    walking_options = [
        "low",
        "moderate",
        "high"
    ]

    trip_days = get_trip_days()

    day_weather = get_choice(
        "Daytime weather "
        "(hot / warm / mild / cool / cold): ",
        weather_options
    )

    night_weather = get_choice(
        "Nighttime weather "
        "(hot / warm / mild / cool / cold): ",
        weather_options
    )

    occasions = get_occasions()

    walking_level = get_choice(
        "Walking level "
        "(low / moderate / high): ",
        walking_options
    )

    (
        top_quantity,
        bottom_quantity,
        underwear_quantity,
        sock_quantity,
        sleepwear_quantity
    ) = calculate_quantities(trip_days)

    tops = []
    bottoms = []
    layers = []
    outerwear = []
    footwear = []
    extras = []

    add_day_weather_items(
        day_weather,
        top_quantity,
        bottom_quantity,
        tops,
        bottoms,
        layers,
        outerwear,
        extras
    )

    add_night_weather_items(
        night_weather,
        layers,
        outerwear
    )

    add_occasion_items(
        occasions,
        tops,
        bottoms,
        footwear,
        extras
    )

    add_walking_items(
        walking_level,
        trip_days,
        footwear
    )

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

    tops = remove_duplicates(tops)
    bottoms = remove_duplicates(bottoms)
    layers = remove_duplicates(layers)
    outerwear = remove_duplicates(outerwear)
    footwear = remove_duplicates(footwear)
    extras = remove_duplicates(extras)

    print()
    print("========================================")
    print("              TRIP SUMMARY")
    print("========================================")
    print("Duration:", trip_days, "days")
    print("Day weather:", day_weather.title())
    print("Night weather:", night_weather.title())
    print("Occasions:", ", ".join(occasions).title())
    print("Walking:", walking_level.title())

    print()
    print("========================================")
    print("          YOUR PACKWISE LIST")
    print("========================================")

    print_category(
        "TOPS",
        tops,
        "No specific tops required"
    )

    print_category(
        "BOTTOMS",
        bottoms,
        "No specific bottoms required"
    )

    print_category(
        "LAYERS",
        layers,
        "No additional layers required"
    )

    print_category(
        "OUTERWEAR",
        outerwear,
        "No heavy outerwear required"
    )

    print_category(
        "FOOTWEAR",
        footwear,
        "No specialised footwear required"
    )

    print_category(
        "EXTRAS + ESSENTIALS",
        extras,
        "No additional extras required"
    )

    print()
    print("========================================")
    print("Pack smarter, not heavier.")
    print("========================================")


main()
