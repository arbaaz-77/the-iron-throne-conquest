house_armies = {"Targaryen": 500, "Lannister": 450, "Stark": 450, "Baratheon": 400}

house_armies["Greyjoy"] = 300
house_armies["Stark"] = 550

for house, troops in house_armies.items():
    print(f"House {house} commands {troops} troops!")

westeros_map = {
    "Targaryen": ["Baratheon", "Tully", "Tyrell"],
    "Stark": ["Tully", "Arryn"],
    "Lannister": ["Tully", "Tyrell"],
    "Baratheon": ["Targaryen", "Tyrell", "Martell"],
    "Tully": ["Stark", "Arryn", "Targaryen", "Tyrell", "Lannister"],
    "Tyrell": ["Lannister", "Tully", "Targaryen", "Baratheon", "Martell"],
    "Martell": ["Tyrell", "Baratheon"],
    "Arryn": ["Stark", "Tully"],
}

print("\n--- The Map of Westeros ---")
print(westeros_map)

# --- Movement Logic ---
current_location = "Stark"
target_location = "Targaryen"

# Check if the target is in the current location's list of borders
if target_location in westeros_map[current_location]:
    print(f"Success: The army marches from {current_location} to {target_location}!")
else:
    print(f"Invalid move! {target_location} does not border {current_location}.")
