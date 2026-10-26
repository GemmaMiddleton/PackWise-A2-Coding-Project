print("========================================")
print("                PACKWISE")
print("      A Personalised Packing Assistant")
print("========================================")

print()
print("Answer a few questions about your trip.")
print("PackWise will use your answers to help plan what to pack.")
print()

trip_days = input("How many days are you travelling for? ")

day_weather = input(
    "What will the daytime weather be like? "
    "(hot / warm / mild / cool / cold): "
)

night_weather = input(
    "What will the nighttime weather be like? "
    "(hot / warm / mild / cool / cold): "
)

occasion = input(
    "What is your main planned occasion? "
    "(casual / beach / dinner / nightlife / formal): "
)

walking_level = input(
    "How much walking will you be doing? "
    "(low / moderate / high): "
)

print()
print("========================================")
print("              TRIP SUMMARY")
print("========================================")
print("Trip duration:", trip_days, "days")
print("Daytime weather:", day_weather)
print("Nighttime weather:", night_weather)
print("Planned occasion:", occasion)
print("Walking level:", walking_level)
print()
print("Thank you. Your trip information has been saved.")
