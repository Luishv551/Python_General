import matplotlib.pyplot as plt

def compound_interest(principal, rate, time, monthly_deposit=0):
    """
    Function to calculate compound interest with an optional monthly deposit.

    Args:
    principal (float): The initial amount of money invested.
    rate (float): Annual interest rate (as a decimal).
    time (int): Time the money is invested for, in years.
    monthly_deposit (float, optional): The amount of money deposited monthly (default is 0).

    Returns:
    float: The amount of money accumulated after compound interest with optional monthly deposit.
    """
    total = principal
    contributions = [principal]  # List to store total contributions over time
    for i in range(time * 12):
        total *= (1 + rate / 12)
        total += monthly_deposit
        contributions.append(contributions[-1] + monthly_deposit)  # Update contributions
    return total, contributions

def main():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the annual interest rate (in decimal): "))
    time = int(input("Enter the time the money is invested for (in years): "))
    monthly_deposit = float(input("Enter the monthly deposit amount (if none, enter 0): "))

    result, _ = compound_interest(principal, rate, time, monthly_deposit)

    print(f"The amount of money accumulated after {time} years is ${result:.2f}")

    # Plotting total contribution vs future value
    future_value, _ = compound_interest(principal, rate, time)

    plt.plot(range(time * 12 + 1), [principal + monthly_deposit * i for i in range(time * 12 + 1)], label='Total Contribution')
    plt.plot(range(time * 12 + 1), [principal * (1 + rate / 12) ** i + monthly_deposit * ((1 + rate / 12) ** i - 1) / (rate / 12) for i in range(time * 12 + 1)], label='Future Value (with compound interest)')

    plt.xlabel('Months')
    plt.ylabel('Amount ($)')
    plt.title('Total Contribution vs Future Value')
    plt.legend()
    plt.grid(True)

    # Save the plot as a JPG file
    plt.savefig('compound_interest_plot.jpg')
    print("Plot saved as compound_interest_plot.jpg")

if __name__ == "__main__":
    main()
