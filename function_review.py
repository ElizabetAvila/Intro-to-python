#Function Review

def death_calculator(name, age):
    average_lifespan = 80
    years_left = average_lifespan - age
    print(f"using an average lifespan of {average_lifespan}, {name} has {years_left} years left to live")
    possible_demise = ["chocked on a grapefruit", "attackedby a rabid owl", "pushed down stairs"]
    cause = random.choice(possible_demise)
    return cause

def main():
    cause = death_calculator(input("Enter your name: "), int(input("Enter your age: ")))
    print("cause of demise: {cause}")
    


if __name__ ==" __main__":
    main()
