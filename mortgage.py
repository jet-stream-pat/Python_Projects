# Generate the monthly outstanding mortgage

# Input: annual interest rate, a floating-point percentage
rate = 0.05

# Input: monthly payment, a positive integer in a currency
payment = 200

# Input: mortgage, a positive number, same currency
mortgage = 1000

# Output: list of monthly outstanding mortgage amounts
outstanding = []

outstanding = outstanding + [mortgage]
while mortgage >0:
    interest = mortgage * rate / 12
    mortgage = mortgage + interest - payment
    print('Outstanding mortgage:', mortgage)
