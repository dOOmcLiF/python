from Currency import Rate

# Получаем курс доллара
curr_rate = Rate('value')
print(curr_rate.usd())

# Получаем изменение курса доллара по сравнению с прошлым значением
curr_diff = Rate('value')
print(curr_diff.usd(diff=True))

# Получаем курс евро
curr_rate_eur = Rate('value')
print(curr_rate_eur.eur())

# Получаем изменение курса евро по сравнению с прошлым значением
curr_diff_eur = Rate('value')
print(curr_diff_eur.eur(diff=True))

r = Rate()

arm_currency_info = r.currency_info('AMD')
print(arm_currency_info)
