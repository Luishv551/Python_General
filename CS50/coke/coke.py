
amount_due = 50

while amount_due > 0:
    print("Amount Due:", amount_due)

    coin = int(input("Insert Coin (5, 10, 25): "))

    if coin in [5, 10, 25]:
        amount_due -= coin
    else:
        print("Invalid coin! Please insert 5, 10, or 25.")

change_owed = abs(amount_due)
print("Change Owed:", change_owed)


