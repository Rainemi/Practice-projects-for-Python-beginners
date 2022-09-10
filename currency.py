#create a function to convert it to the required currency
#collect the amount of currency to be converted
#then create a lamda function for the converter

def main():
    print()

    dollars = eval(input("Enter amount in dollars : "))
    pounds = convert_to_pounds(dollars)
    print("That is ", pounds, "pounds.")

convert_to_pounds = lambda dollars: dollars * 1.16
main()

#Note: you can collect all currency pairs from api and use it for the converter if its o a greater scale. This example only signifies the basic converter   
