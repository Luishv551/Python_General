import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

class RetirementCalculator:
    def __init__(self, principal, rate, time):
        self.principal = principal
        self.rate = rate
        self.time = time

    def calculate_monthly_savings_goal(self, final_amount):
        monthly_rate = self.rate / 12
        n_months = self.time * 12

        monthly_savings = (final_amount - self.principal * (1 + monthly_rate) ** n_months) / \
                          ((1 + monthly_rate) ** n_months - 1) * monthly_rate

        return monthly_savings

    def calculate_total_contribution(self, monthly_savings):
        total_contribution = monthly_savings * self.time * 12
        return total_contribution

    def calculate_total_interest(self, final_amount, total_contribution):
        total_interest = final_amount - total_contribution
        return total_interest

    def plot_graph(self, monthly_savings, final_amount, filename):
        total_contribution = self.calculate_total_contribution(monthly_savings)
        total_values = [self.principal]
        months = list(range(self.time * 12 + 1))
        for i in range(1, self.time * 12 + 1):
            total_values.append(total_values[-1] * (1 + self.rate / 12) + monthly_savings)

        years = [month / 12 for month in months]  # Convert months to years for x-axis

        plt.plot(years, [monthly_savings * i for i in months], label='Total Contribution')
        plt.plot(years, total_values, label='Total Value (Contribution + Interest)')
        plt.xlabel('Years')
        plt.ylabel('Amount ($)')
        plt.title('Total Contribution vs Total Value Over Time')
        plt.legend()
        plt.grid(True)

        # Format y-axis ticks as dollars
        plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter('${x:,.0f}'))

        # Save plot as a jpg file
        plt.savefig(filename)
        print(f"Plot saved as {filename}")

def main():
    principal = float(input("Enter the initial principal amount: "))
    rate = float(input("Enter the annual interest rate (in decimal): "))
    time = int(input("Enter the number of years you plan to work: "))
    final_amount = float(input("Enter the final amount you want to have at retirement: "))
    filename = input("Enter the filename to save the plot (include .jpg extension): ")

    calculator = RetirementCalculator(principal, rate, time)

    monthly_savings = calculator.calculate_monthly_savings_goal(final_amount)
    total_contribution = calculator.calculate_total_contribution(monthly_savings)
    total_interest = calculator.calculate_total_interest(final_amount, total_contribution)

    print(f"To reach your retirement savings goal of ${final_amount:.2f}:")
    print(f"- You should save ${monthly_savings:.2f} per month.")
    print(f"- Total contribution: ${total_contribution:.2f}")
    print(f"- Total interest earned: ${total_interest:.2f}")

    calculator.plot_graph(monthly_savings, final_amount, filename)

if __name__ == "__main__":
    main()
