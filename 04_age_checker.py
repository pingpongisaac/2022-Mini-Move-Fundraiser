# functions go here


# Main routine goes here
tickets_sold = 0

while True:

    name = input("Enter your name / xxx to quit: ")

    if name == "xxx":
        break

    age = int(input("Age: "))

    if 12 <= age <= 120:
        pass
    elif age < 12:
        print("Sorry you are too young for this movie")
        continue
    else:
        print("?? That looks like a typo please try again.")
        continue

    tickets_sold += 1

print("You have sold {} tickets".format(tickets_sold))