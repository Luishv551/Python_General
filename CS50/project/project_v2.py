import matplotlib.pyplot as plt

class CompoundInterestCalculator:
    def __init__(self, principal, rate, time, monthly_deposit=0):
        self.principal = principal
        self.rate = rate
        self.time = time
        self.monthly_deposit = monthly_deposit
        self.contributions = self.calculate_contributions()

    def calculate_contributions(self):
        contributions = [self.principal]  # List to store total contributions over time
        for i in range(self.time * 12):
            self.principal *= (1 + self.rate / 12)
            self.principal += self.monthly_deposit
            contributions.append(self.principal)  # Update contributions
        return contributions

    def plot_graph(self):
        plt.plot(range(self.time * 12 + 1), self.contributions, label='Total Contribution')
        plt.plot(range(self.time * 12 + 1), [self.principal * (1 + self.rate / 12) ** i + self.monthly_deposit * ((1 + self.rate / 12) ** i - 1) / (self.rate / 12) for i in range(self.time * 12 + 1)], label='Future Value (with compound interest)')
        plt.xlabel('Months')
        plt.ylabel('Amount ($)')
        plt.title('Total Contribution vs Future Value')
        plt.legend()
        plt.grid(True)

    def save_plot(self, filename):
        self.plot_graph()
        plt.savefig(filename)
        print(f"Plot saved as {filename}")

def main():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the annual interest rate (in decimal): "))
    time = int(input("Enter the time the money is invested for (in years): "))
    monthly_deposit = float(input("Enter the monthly deposit amount (if none, enter 0): "))
    filename = input("Enter the filename to save the plot (include .jpg extension): ")

    calculator = CompoundInterestCalculator(principal, rate, time, monthly_deposit)
    result = calculator.contributions[-1]
    print(f"The amount of money accumulated after {time} years is ${result:.2f}")

    calculator.save_plot(filename)

if __name__ == "__main__":
    main()
