# 3. FEBRUARY 2023 - PROGRAMMING (PYTHON FUNCTIONS)

# INTRO MESSAGE EHEH ------------------------------------------------------------------------------------------------
print("Hello stranger, welcome to this file.")
continew = input("Type continue to move on..\n")

hello = input("My name is Maria and I will be your operator for today.\n")

inform = input("Before we begin, I need to inform you about this file.\n")

survey = input("This is a survey to prevent the world from dying.\n")

print("We will ask you for a few questions.")
print("\n For the sake of humanity, please answer as genuinely as you can.")

yes = input("Type 'ok' to continue.\n")


# TAB 1 --------------------------------------------------------------------------------------------------------------
loading = input("LOADING...")


# NAME ----------------------------------------------------------------------------------------------------------------
while True:
    name = input("Hey there you! What's your name?\n")
    print(name)
    if name == "Your mom":
        print("My mom is not you. Please try again.")

    elif name == "your mom":
        print("That was not very nice. Please try again.")

    elif name == "Fuck you":
        print("That was not very nice. Please try again.")

    elif name == "fuck you":
        print("That was not very nice. Please try again.")

    elif name == "No":
        print("That was not very nice. Please try again.")

    elif name == "no":
        print("That was not very nice. Please try again.")

    else:
        print("Nice name " + name)
        break


# AGE ------------------------------------------------------------------------------------------------------------------
age = int(input('What is your age...\n'))
print(age)


def check_age(
        age):
    while not age.isnumeric():
        print("Invalid. Please enter a number.")


if age < 18:
    print("Darling, what are you doing here?")
    exit()

if age > 18:
    print("Oh. Hi boomer *sideeye*")


if age == 18:
    print("Just riightt ;D")


# ADDRESS ---------------------------------------------------------------------------------------------------------
while True:
    noGoAddressList: list[str] = ["No", "no", "Yes", "yes", "Nope", "nope", "Yep", "yep", "No way", "no way",
                                  "fuck you", "Fuck you", "fackyou", "Fackyou", "Hehe", "hehe", "Your mom", "your mom"]
    address = input('Type in your address...\n')
    if any(address == word for word in noGoAddressList):
        print("I SAID, PUT IN YOUR GODDAMN ADDRESS!!!! >:(")

    else:
        print(address)
        print("Wow, you live really close to me.")
        print("Whatever you do..\n Don't. Look. Outside.")
        break

#  MILD PANIC ATTACK ---------------------------------------------------------------------------------------------------
while True:
    continew2 = input('Did you look outside?\n')
    nothencontinueList: list[str] = ["No", "no"]
    yesdontcontinueList: list[str] = ["Yes", "yes"]
    if continew2 in yesdontcontinueList:
        print('Oh no.. Hide')
        exit()

    elif continew2 in nothencontinueList:
        print('Good. Ignore the voices.\n')
        print('Keep your focus here.\n')
        break

#  CHOOSE --------------------------------------------------------------------------------------------------------------

print("There are 5 personality archetypes according to psychologist, Mark Moore.\n")
print("They are 'REGULAR', 'STAR', 'CARETAKER', 'DRAMANIC' and 'OBSERVER'.\n")

REGULAR_dict = {
    "archetype name": "REGULAR",
    "traits": "minds their own business, going with the flow and tries to be nice to everyone"
                }
STAR_dict = {
    "archetype name": "STAR",
    "traits": "sought out or wants to be sought after, very extroverted and always wants to "
              "leave a good impression on everyone."
            }
CARETAKER_dict = {
    "archetype name": "CARETAKER",
    "traits": "very caring either outwardly or inwardly, wants the best for everyone, "
              "people pleaser and cannot take care of themselves."
                }
DRAMANIC_dict = {
    "archetype name": "DRAMANIC",
    "traits": "wants to be sought after but isn't, attention seeking, loud "
              "and always picks up a fight both small or big."
                }
OBSERVER_dict = {
    "archetype name": "OBSERVER",
    "traits": "all up on people's business either with subtlety or expressively, doesn't really do anything about"
              "things happening around them and takes no actions. "
                }
while True:
    readDICTS = input('Do you wanna read about them?\n')
    archetypesDictListREGULAR: list[str] = ["REGULAR", "regular"]
    archetypesDictListSTAR: list[str] = ["STAR", "star"]
    archetypesDictListCARETAKER: list[str] = ["CARETAKER", "caretaker"]
    archetypesDictListDRAMANIC: list[str] = ["DRAMANIC", "dramanic"]
    archetypesDictListOBSERVER: list[str] = ["OBSERVER", "observer"]
    nodontcontinueList: list[str] = ["No", "no"]
    yesthencontinueList: list[str] = ["Yes", "yes"]
    if readDICTS in yesthencontinueList:
        print('REGULAR ; STAR ; CARETAKER ; DRAMANIC ; OBSERVER')
        inp = input('Which one would you like to ')
        if inp in archetypesDictListREGULAR:
            print(REGULAR_dict["traits"])
        if inp in archetypesDictListSTAR:
            print(STAR_dict["traits"])
        if inp in archetypesDictListCARETAKER:
            print(CARETAKER_dict["traits"])
        if inp in archetypesDictListDRAMANIC:
            print(DRAMANIC_dict["traits"])
        if inp in archetypesDictListOBSERVER:
            print(OBSERVER_dict["traits"])

    elif readDICTS in nodontcontinueList:
        print('Okay bye, boomer.\n')
        exit()

print("TO BE CONTINUED ....")