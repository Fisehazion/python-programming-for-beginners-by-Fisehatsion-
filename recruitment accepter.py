#clients data receiver website script.
# Fisehatsion Adisu Abute
#it is easy to use.
x = int(input("Enter a day (1<=x<=30): "))

if x >= 1 and x <= 30:
    if 1 <=x <=5:
        print("Recruitment day and come in-person to out office at 4Kilo.")    
    elif x >= 6:
        print("\n Not Recruitment day of the month")
        print("You are misinformed. Please check our website for any updates.")
        print("The spot is over for now. Please write your personal info below.")
        name = input("Write your name here: ")
        phone = input(" put your phone number here, please!: ")
        print("Thank you for visiting us, " + name + "!")
    else:
        print("Not applicable")
else:
    print("Invalid input. Please enter a day between 1 and 30.")
print("https://fisehatsion-adisu-abute.hi.link")
