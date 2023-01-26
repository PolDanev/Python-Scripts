from forex_python.converter import CurrencyRates

c = CurrencyRates()

amount = int(input("Enter your currency amount: "))
print()

from_currency = input("From currency: ")
to_currency = input("To currency: ")

result = c.convert(from_currency, to_currency, amount)
print()

print(f"From currency {from_currency} <=> to currency {to_currency}")
print(f"You have {result:.2f} amount!")
