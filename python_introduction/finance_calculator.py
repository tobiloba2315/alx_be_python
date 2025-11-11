monthly_income = input("Enter your monthly income: ")
monthly_income = input("Enter your monthly income: ")
monthly_expenses = input("Enter your total monthly expenses: ")
monthly_savings = float(monthly_income) - float(monthly_expenses)
annual_savings = monthly_savings * 12
savings_with_interest = annual_savings * 1.05
print(f"Annual savings with 5% interest: ${savings_with_interest:.2f}")
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(f"Projected savings after one year with 5% interest: ${projected_savings:.2f}")
print(f"Monthly savings: ${monthly_savings:.2f}")
print(f"Projected annual savings after including interest: ${savings_with_interest:.2f}")