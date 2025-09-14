# Personal Finance Calculator
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))
monthly_savings = income - expenses
print(f"Your monthly savings are: ${int(monthly_savings)}")

annual_savings_no_interest = monthly_savings * 12
interest_earned = annual_savings_no_interest * 0.05
projected_savings = annual_savings_no_interest + interest_earned

print(f"Projected savings after one year, with interest, is ${int(projected_savings)}")




