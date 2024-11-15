from Currency import Rate

rate_value = Rate('value')
rate_full = Rate('full')
rate_name = Rate('name')

print(rate_value.usd())
print(rate_name.eur())

print(rate_value.usd(diff=True))

print(rate_name.get_currency('GBP'))

print(rate_name.get_max_currency())
print(rate_name.get_min_currency())

usd_history = rate_value.get_usd_history(weeks=2)
for date, value in usd_history.items():
    print(f"Курс доллара на {date}: {value}")

eur_history = rate_value.get_currency_history('EUR', weeks=1)
for date, value in eur_history.items():
    print(f"Курс евро на {date}: {value}")