
print("Welcome to the Roller Coaster!")

height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))

if height >= 120:
    if age >= 12:
        print("You can ride the roller coaster!")
    else:
        print("Sorry, you need to be at least 12 years old to ride.")
else:
    print("Sorry, you need to be at least 120 cm tall to ride.")