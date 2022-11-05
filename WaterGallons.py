Code = input('Enter a code ').lower()
Sd = int(input("Enter Customer's beginning meter reading: "))
Ed = int(input(f"The customer's ending meter reading:\t  "))
if(0 < Sd < 999999999) and (0 < Ed < 999999999) and (Code == 'r') or (Code == 'c') or (Code == 'i'):
    if (Sd > Ed):
        Gallons = (((999999999 + Ed) - Sd) + 1) * .1
    elif (Sd < Ed):
        Gallons = (Ed - Sd) * .1
    if (Code == 'r'):
        Cost = 5 + (Gallons * .0005)
    if (Code == 'c') and (Gallons < 4000000):
        Cost = 1000
    elif (Gallons > 4000000):
        Cost = 1000 + ((Gallons - 4000000) * .00025)
    if (Code == 'i') and (Gallons < 4000000):
        Cost = 1000
    elif (Gallons > 4000000) and (Gallons < 10000000):
        Cost = 2000
    elif (Gallons > 10000000):
        Cost = 2000 + ((Gallons - 10000000) * .00025)
    print(f"Customer Code: {Code}")
    print("Beginning meter reading: {:0>9}".format(Sd))
    print("Ending meter reading:\t {:0>9}".format(Ed))
    print(f"Gallons of water used: {Gallons:.1f}")
    print(f"Amount Billed: ${Cost:.2f}")
else:
        print("Invalid Entry")
        print("Gallons of water used: 0.0")
        print("Amount billed: 0.0 ")