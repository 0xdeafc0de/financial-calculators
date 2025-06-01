# Calculate future value of money.
def calculate_fvm(present_value, annual_rate, years):
    """
    Calculate Future Value of Money (FVM)
    :param present_value: Current value (float or int)
    :param annual_rate: Annual interest or inflation rate (as decimal, e.g., 0.06 for 6%)
    :param years: Time period in years
    :return: Future value
    """
    #fvm = present_value * (1 - annual_rate) ** years
    # Future value is adjusted for inflation; value decreases as inflation erodes purchasing power over time
    fvm = present_value / ((1 + annual_rate) ** years)
    return fvm

# Example input
# Present Value
pv = float(input("Enter Present Value (e.g., 20000000 for ₹2Cr): ").strip() or 20000000)

#Annual Inflation Rate
air = float(input("Enter avg annual inflation rate (e.g., 6 for 6%): ").strip() or 6)

# Time period
years = float(input("Enter number of years after which future value is calculated: ").strip() or 20)

print(f"Present Value {pv}, Annual inflation rate {air}%/yr, time period {years} years")

air = air / 100

fvm = calculate_fvm(pv, air, years)
print(f"Future Value after {years} years: ₹{fvm:,.2f}")

