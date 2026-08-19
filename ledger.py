house_armies = {"Targaryen": 500, "Lannister": 450, "Stark": 450, "Baratheon": 400}

house_armies["Greyjoy"] = 300
house_armies["Stark"] = 550

for house, troops in house_armies.items():
    print(f"House {house} commands {troops} troops!")
