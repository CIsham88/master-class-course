gender_options = ["male", "female", "prefer not to say"]

name = input("What is your name? ")
while name.isalpha() is False:
    print("I'm sorry, that is not a viable name.")
    name = input("What is your name? ")
age = str(input("What is your age? "))
while age.isdigit() is False:
    print("Please use only numbers for your age.")
    age = input("What is your age? ")
gender = input("Are you male, female or do you "
               "prefer not to say? ").casefold()
while gender not in gender_options:
    gender = input('Please enter "Male", "Female" or '
                   '"Prefer not to say" ').casefold()
print()
print("-" * 10)
print()


def say_hi():
    print("Hello " + name.capitalize() + "! \nYou are "
          + str(age) + " years old.")
    if gender == "female":
        print("You are a woman.\n\n"
              "Have a nice day!")
    elif gender == "male":
        print("You are a man.\n\n"
              "Have a nice day!")
    else:
        print("Have a nice day!")


say_hi()
print()
print("-" * 10)
