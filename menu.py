value = 1
gc = 0
ga = 0
al = 0
et = 0
amount = 0
while value != 0:
    print("[Menu of fuel!]\nSelect the fuel.")
    print("1 - Gasoline common = 5.89.\n2 - Gasoline Added = 5.20.")
    print("3 - Alcohol = 3.67.\n4 - Ethanol = 4.38.\n0 - for leave and close program.")

    value = int(input(""))
    if value == 1:
        print("Selected: Gasoline common.")
        gc = gc + 5.89
    elif value == 2:
        print("Selected: Gasoline Added.")
        ga = ga + 5.20
    elif value == 3:
        print("Selected: Alcohol.")
        al = al + 3.67
    elif value == 4:
        print("Selected: Ethanol.")
        et = et + 4.38
    else:
        print("Selecione alguma opcao da lista.")

amount = gc + ga + al + et
print("Check the balance of day.")
print(f"Gasoline Common: R${gc:,.2f}\nGasoline Added: R${ga:,.2f}")
print(f"Alcohol: R${al:,.2f}\nEthanol: R${et:,.2f}\nProfit total: R${amount:,.2f}")