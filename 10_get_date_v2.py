from datetime import date

# get today date
today = date.today()

# get day/month/year as individual
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

heading = "The current date is {}/{}/{}".format(day, month, year)
filename = "MMF_{}_{}_{}".format(year, month, day)

# heading
print(heading)
print("The filename will be {}.txt".format(filename))