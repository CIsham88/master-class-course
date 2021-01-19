heroes = ["Luke Skywalker".casefold(),
          "Indiana Jones".casefold(),
          "James Bond".casefold(),
          "Gandalf".casefold(),
          ]

choice = input("\nPlease choose an option from the list below: "
               "\n\n"
               "1. Luke Skywalker\n"
               "2. Indiana Jones\n"
               "3. James Bond\n"
               "4. Gandalf\n"
               "0. Quit\n\n")

while choice not in "01234" and choice.casefold() not in heroes:
    choice = input("\nInvalid option.\n"
                   "Please choose an option from the list below: "
                   "\n\n"
                   "1. Luke Skywalker\n"
                   "2. Indiana Jones\n"
                   "3. James Bond\n"
                   "4. Gandalf\n"
                   "0. Quit\n\n")

if choice == "0":
    print("You have Quit")
elif choice.casefold() in heroes:
    place = heroes.index(choice.casefold()) + 1
    print("Congratulations! You have selected "
          "#{}, {}!".format(place, choice.title()))
else:
    selection = int(choice) - 1
    print("Congratulations! You have selected #{0}, {1}!"
          "".format(choice, heroes[selection].title()))
