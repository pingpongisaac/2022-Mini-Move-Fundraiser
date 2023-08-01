# functions


# main routine
while True:
    want_instructions = input("Do you want instructions? ").lower()

    if want_instructions == "yes" or want_instructions == "y":
        print("Instructions go here")
    elif want_instructions == "no" or want_instructions == "n":
        pass
    else:
        print("please answer yes / no")

print("We are Done")
