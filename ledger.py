import random

house_armies = {
    "Targaryen": 500,
    "Lannister": 450,
    "Stark": 450,
    "Baratheon": 400,
    "Tyrell": 500,
    "Martell": 300,
    "Arryn": 400,
}

house_armies["Tully"] = 350
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
target_location = "Tully"

# Check if the target is in the current location's list of borders
if target_location in westeros_map[current_location]:
    print(f"Success: The army marches from {current_location} to {target_location}!")
else:
    print(f"Invalid move! {target_location} does not border {current_location}.")


# --- Combat System ---
def battle(attacker, defender):
    print(f"\n⚔️ Battle begins: House {attacker} vs House {defender}! ⚔️")

    # 1. Pull the base troops from the ledger
    attacker_troops = house_armies[attacker]
    defender_troops = house_armies[defender]

    # 2. Add a random battlefield advantage (rolling a 100-sided die)
    # random.randint(1, 100) picks a random integer between 1 and 100.
    attacker_score = attacker_troops + random.randint(1, 100)
    defender_score = defender_troops + random.randint(1, 100)

    # 3. Determine the winner
    if attacker_score > defender_score:
        print(
            f"House {attacker} wins the battle with a score of {attacker_score} to {defender_score}!"
        )
    else:
        print(
            f"House {defender} holds the line with a score of {defender_score} to {attacker_score}!"
        )


# --- The Game Loop ---
print("\n" + "=" * 40)
print(" Welcome to The Iron Throne Conquest!")
print("=" * 40)

while True:
    # 1. Ask the user, strip spaces, and make it lowercase
    command = input("\nEnter command (or 'quit' to exit): ").strip().lower()

    if command == "quit":
        print("You have yielded the Iron Throne. Farewell!")
        break

    # 2. Split the command into a list of words
    parts = command.split()

    # 3. Guard clause: If they just pressed Enter without typing, restart the loop
    if len(parts) == 0:
        continue

    # 4. Isolate the main action (the first word)
    action = parts[0]  # Hint: Lists start at index 0!

    # 5. Handle the "march" command
    if action == "march" and len(parts) == 3:
        attacker = parts[1].capitalize()
        defender = parts[2].capitalize()

        # Guard clause: Do these houses actually exist?
        if attacker not in house_armies or defender not in house_armies:
            print("Invalid order! One or both of those houses do not exist.")
            continue  # Skips the rest of the loop and starts over

        # Movement Validation (from Milestone 2)
        if defender in westeros_map[attacker]:
            # The move is valid! Trigger the combat system.
            battle(attacker, defender)
        else:
            print(f"Invalid move! {defender} does not border {attacker}.")
