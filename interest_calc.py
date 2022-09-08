#collect all necessary input i.e principal,annual interest rate,years
# create a function to calculate the payment


def calc():
    print("")

    principal = float(input("Enter the amount borrowed : "))
    irate = float(input("Enter the annual interest rate : "))
    years = int(input("Enter the amount of years : "))

    monthly_interest_rate = irate / 1200
    amount_of_months = years * 12
    monthly_payment = principal * monthly_interest_rate / (1-(1 +monthly_interest_rate)** (- amount_of_months))

    print("The monthly payment for this loan is : %.2f"% monthly_payment)

calc()
