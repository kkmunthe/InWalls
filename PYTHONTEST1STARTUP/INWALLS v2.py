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


def check_age(age):
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
