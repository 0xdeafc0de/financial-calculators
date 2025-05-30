#
# Corpus longetivity estimator - Find out how long your hard earned savings
# will last with inflation and the RoI you get on the remaining corpus.
#
import numpy as np

# user inputs with default (if no input provided)
corpus = float(input("Enter initial corpus amount (e.g., 20000000 for ₹2Cr): ").strip() or 20000000)
yearly_exp = float(input("Enter yearly withdrawl amount (e.g., 1200000 for ₹1L/month): ").strip() or 1200000)
roi = float(input("Enter avg annual RoI (in %, e.g., 7.5: ").strip() or 8)
inflation_rate = float(input("Enter avg inflation rate (in %, e.g., 5): ").strip() or 5)

print(f"Using corpus {corpus}, yearly expenses {yearly_exp}, rate-of-int {roi}%/yr and inflation rate {inflation_rate}%")

roi = roi / 100
inflation_rate = inflation_rate / 100

# Convert annual to monthly rates
monthly_roi = (1 + roi) ** (1/12) - 1
monthly_inflation = (1 + inflation_rate) ** (1/12) - 1

# Convert yearly expense to monthly
monthly_exp = yearly_exp / 12

# Simulation loop to determine how long the corpus lasts
months = 0
while corpus > 0:
    corpus = corpus * (1 + monthly_roi) - monthly_exp
    if corpus <= 0:
        break

    monthly_exp *= (1 + monthly_inflation)
    months += 1

# Convert months to Year + Months
years = months // 12
remaining_months = months % 12

print(f"\n Corpus will last {years} years and {remaining_months} months.")


