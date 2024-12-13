#Kenia Avila
#12-4-24
#making a video game

# Zork-Style Text Adventure: Character Selection

def show_intro():
    print("Welcome to the Zork-style Adventure!")
    print("You will embark on a journey filled with mystery and danger.")
    print("But first, choose your character wisely!\n")

def choose_character():
    print("1. Knight Aloys")
    print("   - Strength: 90")
    print("   - Speed: Moderate")
    print("   - Starting Item: Sword\n")

    print("2. Wizard Ranulf")
    print("   - Strength: 65")
    print("   - Speed: Moderate")
    print("   - Starting Item: Magic Staff\n")

    print("3. Crook Cassian")
    print("   - Strength: 75")
    print("   - Speed: High")
    print("   - Starting Item: Dagger\n")

    while True:
        choice = input("Choose your character (1/2/3): ").lower()
        if choice == 'exit':
            quit_game()
        if choice in ['1', '2', '3']:
            return int(choice)
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
#Zork-Style enemy 

def combat(player_name, player_strength, enemy_name, enemy_damage):
    print(f"\nOh no! A {enemy_name} appears!")
    print(f"Prepare for battle, {player_name}!")
    
    while player_strength > 0:
        print(f"\nYour strength: {player_strength}")
        action = input("Do you fight or run? (fight/run): ").lower()
        if action == "exit":
            quit_game()
        if action == "fight":
            print(f"You attack the {enemy_name}!")
            print(f"The {enemy_name} attacks back and reduces your strength by {enemy_damage}!")
            player_strength -= enemy_damage
            if player_strength <= 0:
                print("\nYou have been defeated by the {enemy_name}. Your adventure ends here!")
                return False
            else:
                print(f"You successfully defeat the {enemy_name}!")
                return True
        elif action == "run":
            print(f"You escape from the {enemy_name}, but it might cost you later.")
            return True
        else:
            print("Invalid choice. Please select 'fight' or 'run'.")
    return False

def enter_cave(name, item, strength):
    print(f"\nAs the {name}, you step boldly into the cave with your {item}.")
    print("The air is damp, and the darkness surrounds you.")
    print("Suddenly, you feel something moving in the shadows...")
    if combat(name, strength, "Arachne", 30):
        print("You emerge from the cave victorious but tired. The adventure continues!")
    else:
        print("Your journey ends here.")

def cross_river(name, item, strength):
    print(f"\nThe {name} approaches a wide river with strong currents.")
    print(f"Using your {item}, you carefully wade across the river.")
    print("But halfway through, something stirs in the water...")
    if combat(name, strength, "Horned Serpent", 25):
        print("You make it to the other side safely! A treasure chest awaits.")
    else:
        print("Your journey ends here.")

def go_into_forest(name, item, strength):
    print(f"\nThe {name} decides to explore the dense forest nearby.")
    print(f"With your {item} in hand, you push through the thick foliage.")
    print("Suddenly, you hear a loud screech from above...")
    if combat(name, strength, "Simurgh", 20):
        print("The forest remains quiet as you continue your journey with a magical amulet.")
    else:
        print("Your journey ends here.")
#Zork-Style path

def choose_new_path(name, item, strength):
    print("\nYou decide not to enter the cave. What will you do instead?")
    print("1. Cross the river")
    print("2. Go into the forest")

    while True:
        choice = input("Choose your action (1/2): ").lower()
        if choice == 'exit':
            quit_game()
        if choice == '1':
            cross_river(name, item, strength)
            break
        elif choice == '2':
            go_into_forest(name, item, strength)
            break
        else:
            print("Invalid choice. Please select 1 or 2.")

def start_adventure(character):
    if character == 1:
        name = "Knight Aloys"
        item = "Sword"
        strength = 90
    elif character == 2:
        name = "Wizard Ranulf"
        item = "Magic Staff"
        strength = 65
    elif character == 3:
        name = "Crook Cssian"
        item = "Dagger"
        strength = 75

    print(f"\nYou have chosen the {name}!")
    print(f"Your adventure begins with a trusty {item} in your hand.\n")
    print("You find yourself at the entrance of a dark cave. A sign reads:")
    print("'Only the bold shall pass.'")
    print("What will you do?")
    print("1. Enter the cave")
    print("2. Walk away and search for another path")

    while True:
        action = input("Choose your action (1/2): ").lower()
        if action == 'exit':
            quit_game()
        if action == '1':
            enter_cave(name, item, strength)
            break
        elif action == '2':
            choose_new_path(name, item, strength)
            break
        else:
            print("Invalid choice. Please select 1 or 2.")
def quit_game():
    print("\nThank you for playing! Your adventure ends here. Goodbye!")
    exit()

# Main game loop
def main():
    show_intro()
    character = choose_character()
    start_adventure(character)

if __name__ == "__main__":
    main()
