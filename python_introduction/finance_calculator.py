# Monthly Savings
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))
monthly_savings = income - expenses
print(f"Your monthly savings are: ${monthly_savings}")

# Projected Annual Savings
annual_savings_no_interest = monthly_savings * 12
projected_savings = annual_savings_no_interest * (1 + 0.05)
print(f"Projected savings after one year, with interest, is ${projected_savings:.2f}")
# Monthly Savings
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))
monthly_savings = income - expenses
print(f"Your monthly savings are: ${monthly_savings:.2f}")

# Projected Annual Savings
annual_savings_no_interest = monthly_savings * 12
projected_savings = (monthly_savings * 12) * (1 + 0.05)

print(f"Projected savings after one year, with interest, is ${projected_savings:.2f}")


