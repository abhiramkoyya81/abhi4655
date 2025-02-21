def convert_currency(amount, from_currency, to_currency, conversion_rates):
    if (from_currency, to_currency) in conversion_rates:
        rate = conversion_rates[(from_currency, to_currency)]
        converted_amount = amount * rate
        return converted_amount
    else:
        return "Conversion rate not available."

conversion_rates = {
    ('USD', 'EUR'): 0.92,  
    ('USD', 'INR'): 83.25,  
    ('USD', 'GBP'): 0.81,   
    ('EUR', 'USD'): 1.09,   
    ('EUR', 'INR'): 90.42,  
    ('EUR', 'GBP'): 0.88,   
    ('INR', 'USD'): 0.012, 
    ('INR', 'EUR'): 0.011, 
    ('INR', 'GBP'): 0.0096 
}

amount = float(input("Enter the amount to convert: "))
from_currency = input("Enter the currency you are converting from (e.g., USD, EUR, INR, GBP): ").upper()
to_currency = input("Enter the currency you want to convert to (e.g., USD, EUR, INR, GBP): ").upper()

converted_amount = convert_currency(amount, from_currency, to_currency, conversion_rates)

if isinstance(converted_amount, float):
    print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}.")
else:
    print(converted_amount)
