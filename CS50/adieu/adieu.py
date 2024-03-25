names = []

while True:
    try:
        new_name = input("Name: ").strip()
        names.append(new_name)

    except EOFError:
        break

if len(names) == 1:
    print(f"\nAdieu, adieu, to {names[0]}")

elif len(names) == 2:
    print(f"\nAdieu, adieu, to {names[0]} and {names[1]}")

elif len(names) == 3:
    print(f"\nAdieu, adieu, to {names[0]}, {names[1]}, and {names[2]}")

elif len(names) >= 4:
    print("\nAdieu, adieu, to ", end="")

    name_index = 0
    for name in names:
        if name_index < (len(names)-1):
            print(f"{name}, ", end="")
        else:
            print(f"and {name}")

        name_index += 1
