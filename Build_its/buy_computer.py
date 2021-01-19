available_parts = ["Computer",
                   "Monitor",
                   "Keyboard",
                   "Mouse",
                   "Mouse mat",
                   "HDMI cable",
                   "DVD drive",
                   "Microphone",
                   "Speakers"
                   ]
#valid_choices = [str(i) for i in range(1, len(available_parts) +1)]
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))

current_choice = "-"
computer_parts = []     # Create an empty list

while current_choice != "0":
    if current_choice in valid_choices:
        print("Adding {}".format(current_choice))
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        computer_parts.append(chosen_part)
    else:
        print("Please add options from the list below:\n"
              "When finished press '0'\n")
        for number, part in enumerate(available_parts):
            print("{0}: {1}".format(number + 1, part))

    current_choice = input()

print(computer_parts)
