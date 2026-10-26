# ==========================================
# PACKWISE
# A Personalised Packing Assistant
# ==========================================

def print_header():
    print()
    print("==========================================")
    print("                 PACKWISE")
    print("       A Personalised Packing Assistant")
    print("==========================================")
    print()


def get_positive_number(question):
    while True:
        answer = input(question).strip()

        if answer.isdigit():
            number = int(answer)

            if number > 0:
                return number

        print()
        print("Please enter a whole number greater than 0.")
        print()


def get_choice(question, choices):
    while True:
        answer = input(question).lower().strip()

        if answer in choices:
            return answer

        print()
        print("That option is not recognised.")
        print("Choose from:", ", ".join(choices))
        print()


def get_occasions():
    choices = [
        "casual",
        "beach",
        "dinner",
        "nightlife",
        "formal"
    ]

    while True:
        print()
        print("You can enter more than one occasion.")
        print("Separate each occasion using a comma.")

        answer = input(
            "Planned occasions "
            "(casual / beach / dinner / nightlife / formal): "
        ).lower()

        raw_occasions = answer.split(",")

        occasions = []
        invalid_occasions = []

        for occasion in raw_occasions:
            occasion = occasion.strip()

            if occasion in choices:
                if occasion not in occasions:
                    occasions.append(occasion)

            elif occasion != "":
                invalid_occasions.append(occasion)

        if (
            len(occasions) > 0
            and len(invalid_occasions) == 0
        ):
            return occasions

        print()

        if len(invalid_occasions) > 0:
            print(
                "Unrecognised option(s):",
                ", ".join(invalid_occasions)
            )

        print(
            "Please use only:",
            ", ".join(choices)
        )


def calculate_quantities(trip_days):
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

    return (
        top_quantity,
        bottom_quantity,
        underwear_quantity,
        sock_quantity,
        sleepwear_quantity
    )


def add_unique(packing_list, item):
    if item not in packing_list:
        packing_list.append(item)


def apply_day_weather_rules(
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
        add_unique(
            tops,
            str(top_quantity)
            + " lightweight breathable tops"
        )

        add_unique(
            bottoms,
            str(bottom_quantity)
            + " pairs of shorts or lightweight bottoms"
        )

        add_unique(extras, "Sunglasses")
        add_unique(extras, "Sun hat")

    elif weather == "warm":
        add_unique(
            tops,
            str(top_quantity)
            + " T-shirts or lightweight tops"
        )

        add_unique(
            bottoms,
            str(bottom_quantity)
            + " lightweight bottoms"
        )

        add_unique(
            layers,
            "1 optional light layer"
        )

    elif weather == "mild":
        add_unique(
            tops,
            str(top_quantity)
            + " everyday tops"
        )

        add_unique(
            bottoms,
            str(bottom_quantity)
            + " pairs of jeans or trousers"
        )

        add_unique(layers, "1 light jumper")

    elif weather == "cool":
        add_unique(
            tops,
            str(top_quantity)
            + " long-sleeve or warm tops"
        )

        add_unique(
            bottoms,
            str(bottom_quantity)
            + " pairs of long pants"
        )

        add_unique(layers, "1-2 warm jumpers")
        add_unique(
            outerwear,
            "1 light-to-medium jacket"
        )

    elif weather == "cold":
        add_unique(
            tops,
            str(top_quantity)
            + " thermal or warm tops"
        )

        add_unique(
            bottoms,
            str(bottom_quantity)
            + " pairs of warm trousers"
        )

        add_unique(layers, "2 warm layering pieces")
        add_unique(outerwear, "1 insulated coat")
        add_unique(
            extras,
            "Cold-weather accessories"
        )


def apply_night_weather_rules(
    weather,
    layers,
    outerwear
):
    if weather == "hot":
        return

    elif weather == "warm":
        add_unique(
            layers,
            "1 lightweight evening layer"
        )

    elif weather == "mild":
        add_unique(
            layers,
            "1 cardigan or light evening jumper"
        )

    elif weather == "cool":
        add_unique(
            layers,
            "1 warm evening jumper"
        )
        add_unique(
            outerwear,
            "1 evening jacket"
        )

    elif weather == "cold":
        add_unique(
            layers,
            "1 heavy evening layer"
        )
        add_unique(
            outerwear,
            "1 warm evening coat"
        )


def apply_occasion_rules(
    occasions,
    tops,
    bottoms,
    footwear,
    extras
):
    for occasion in occasions:
        if occasion == "casual":
            add_unique(
                tops,
                "1 versatile casual top"
            )
            add_unique(
                bottoms,
                "1 versatile casual bottom"
            )

        elif occasion == "beach":
            add_unique(
                extras,
                "1-2 sets of swimwear"
            )
            add_unique(
                extras,
                "1 beach cover-up"
            )
            add_unique(
                footwear,
                "1 pair of sandals or slides"
            )

        elif occasion == "dinner":
            add_unique(
                tops,
                "1 smart evening top"
            )
            add_unique(
                bottoms,
                "1 smart evening bottom"
            )
            add_unique(
                footwear,
                "1 pair of dinner shoes"
            )

        elif occasion == "nightlife":
            add_unique(
                tops,
                "1 going-out top"
            )
            add_unique(
                bottoms,
                "1 evening bottom"
            )
            add_unique(
                footwear,
                "1 pair of going-out shoes"
            )

        elif occasion == "formal":
            add_unique(
                extras,
                "1 complete formal outfit"
            )
            add_unique(
                footwear,
                "1 pair of formal shoes"
            )


def apply_walking_rules(
    walking_level,
    trip_days,
    footwear
):
    if walking_level == "low":
        add_unique(
            footwear,
            "1 pair of comfortable everyday shoes"
        )

    elif walking_level == "moderate":
        add_unique(
            footwear,
            "1 pair of comfortable sneakers"
        )

    elif walking_level == "high":
        add_unique(
            footwear,
            "1 pair of supportive walking shoes"
        )

        if trip_days >= 6:
            add_unique(
                footwear,
                "1 backup pair of comfortable shoes"
            )


def add_essentials(
    trip_days,
    underwear_quantity,
    sock_quantity,
    sleepwear_quantity,
    extras
):
    add_unique(
        extras,
        str(underwear_quantity)
        + " pairs of underwear"
    )

    add_unique(
        extras,
        str(sock_quantity)
        + " pairs of socks"
    )

    add_unique(
        extras,
        str(sleepwear_quantity)
        + " sleepwear set(s)"
    )

    if trip_days >= 7:
        add_unique(extras, "Laundry bag")


def create_packing_notes(
    trip_days,
    day_weather,
    night_weather,
    walking_level,
    occasions
):
    notes = []

    if trip_days <= 3:
        notes.append(
            "This is a short trip, so prioritise versatile pieces "
            "that can be worn more than once."
        )

    elif trip_days >= 10:
        notes.append(
            "For a longer trip, consider rewearing versatile pieces "
            "instead of packing a completely new outfit every day."
        )

    if (
        day_weather == "hot"
        and (
            night_weather == "cool"
            or night_weather == "cold"
        )
    ):
        notes.append(
            "There is a large day-to-night temperature change, "
            "so keep an extra layer accessible in the evening."
        )

    if walking_level == "high":
        notes.append(
            "Comfortable footwear should be prioritised because "
            "your trip involves a high amount of walking."
        )

    if len(occasions) >= 3:
        notes.append(
            "You have several different occasions planned. "
            "Choose versatile items that can work across multiple outfits."
        )

    if (
        "formal" in occasions
        or "dinner" in occasions
    ):
        notes.append(
            "Pack occasion-specific clothing carefully so it "
            "stays clean and presentable during travel."
        )

    if len(notes) == 0:
        notes.append(
            "Your trip has relatively straightforward packing needs. "
            "Focus on versatile clothing rather than unnecessary extras."
        )

    return notes


def display_category(
    category_name,
    items,
    empty_message
):
    print()
    print(category_name.upper())
    print("-" * 42)

    if len(items) == 0:
        print("•", empty_message)
    else:
        for item in items:
            print("•", item)


def display_trip_summary(
    trip_days,
    day_weather,
    night_weather,
    occasions,
    walking_level
):
    print()
    print("==========================================")
    print("               TRIP SUMMARY")
    print("==========================================")
    print("Duration:", str(trip_days) + " days")
    print("Daytime weather:", day_weather.title())
    print("Nighttime weather:", night_weather.title())
    print(
        "Occasions:",
        ", ".join(occasions).title()
    )
    print("Walking level:", walking_level.title())


def display_notes(notes):
    print()
    print("PACKWISE NOTES")
    print("-" * 42)

    for note in notes:
        print("•", note)


def main():
    print_header()

    print(
        "PackWise creates a personalised clothing list "
        "using your trip conditions."
    )
    print()
    print(
        "Answer the following questions as accurately "
        "as possible."
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

    trip_days = get_positive_number(
        "How many days are you travelling for? "
    )

    print()

    day_weather = get_choice(
        "Daytime weather "
        "(hot / warm / mild / cool / cold): ",
        weather_options
    )

    print()

    night_weather = get_choice(
        "Nighttime weather "
        "(hot / warm / mild / cool / cold): ",
        weather_options
    )

    occasions = get_occasions()

    print()

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

    apply_day_weather_rules(
        day_weather,
        top_quantity,
        bottom_quantity,
        tops,
        bottoms,
        layers,
        outerwear,
        extras
    )

    apply_night_weather_rules(
        night_weather,
        layers,
        outerwear
    )

    apply_occasion_rules(
        occasions,
        tops,
        bottoms,
        footwear,
        extras
    )

    apply_walking_rules(
        walking_level,
        trip_days,
        footwear
    )

    add_essentials(
        trip_days,
        underwear_quantity,
        sock_quantity,
        sleepwear_quantity,
        extras
    )

    notes = create_packing_notes(
        trip_days,
        day_weather,
        night_weather,
        walking_level,
        occasions
    )

    display_trip_summary(
        trip_days,
        day_weather,
        night_weather,
        occasions,
        walking_level
    )

    print()
    print("==========================================")
    print("             YOUR PACKWISE LIST")
    print("==========================================")

    display_category(
        "Tops",
        tops,
        "No specialised tops required"
    )

    display_category(
        "Bottoms",
        bottoms,
        "No specialised bottoms required"
    )

    display_category(
        "Layers",
        layers,
        "No additional layers required"
    )

    display_category(
        "Outerwear",
        outerwear,
        "No heavy outerwear required"
    )

    display_category(
        "Footwear",
        footwear,
        "No specialised footwear required"
    )

    display_category(
        "Extras + Essentials",
        extras,
        "No additional extras required"
    )

    display_notes(notes)

    print()
    print("==========================================")
    print("              PACKWISE COMPLETE")
    print("          Pack smarter, not heavier.")
    print("==========================================")
    print()


main()
