def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Split the IP address into its components
    components = ip.split('.')

    # Check if there are exactly 4 components
    if len(components) != 4:
        return False

    # Check each component
    for component in components:
        # Check if each component is a valid integer
        if not component.isdigit():
            return False
        # Convert the component to an integer
        num = int(component)
        # Check if the integer is within the valid range [0, 255]
        if num < 0 or num > 255:
            return False

    # If all checks pass, the IP address is valid
    return True


if __name__ == "__main__":
    main()
