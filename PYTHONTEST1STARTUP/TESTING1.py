# PYTHON TESTING KODE FT. GITHUB
# AF KRISTINE


# NAME
name = input("Hey there you! What's your name?\n")
print(name)
print("Nice name "+name)


#AGE
age = int(input('Type in your age...\n'))
print(age)

if age < 17:
    print("Juicy age <3")


if age > 17:
       print("Too old eww")


if age == 17:
    print("Just riightt ;D")

# ADDRESS
while True:
    noGoAddressList: list[str] = ["No","no","Yes","yes","Nope","nope","Yep","yep","No way","no way","fuck you","Fuck you","fackyou","Fackyou","Hehe","hehe","Your mom","your mom"]
    address = input('Type in your address...\n')
    if any(address==word for word in noGoAddressList):
        print("I SAID, PUT IN YOUR FUCKING ADDRESS!!!! >:(")

    else:
        print(address)
        print("Wow, you live really close to me.")
        print("Look outside :)")
        break





