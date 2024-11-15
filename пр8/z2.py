from Currency import Rate  

print("Получение полной информации о курсе доллара")
curr = Rate('full')  
print(curr.usd())  

print("Получение изменения курса доллара")
curr = Rate('value')  
print(curr.usd(diff=False))

print("Получение информации о произвольной валюте")
print(curr.get_currency_info('EUR'))

print("Получение валют с максимальной и минимальной стоимостью")
max_currency, min_currency = curr.max_min_currency()  
print(max_currency)  
print(min_currency)  

print("Получение курса доллара за 2 недели")
usd_rates = curr.get_usd_rate_over_weeks(2)  
print(usd_rates)  

print("Получение курса евро за 3 недели")
eur_rates = curr.get_currency_rate_over_weeks('EUR', 3)  
print(eur_rates)