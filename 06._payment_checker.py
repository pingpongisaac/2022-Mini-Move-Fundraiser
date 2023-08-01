# functions
def cash_credit(question):

    while True:
        response = input(question).lower()

        if response == "cash" or response == "ca":
            return "yes"
        elif response == "credit" or response == "cr":
            return "credit"
        else:
            print("please choose a valid payment option")


# main routine
while True:
    payment_method = cash_credit("Choose a payment method, cash or credit: ")


    print("You chose", payment_method)

    print("program continues")
    print()
