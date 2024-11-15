import requests
from datetime import datetime, timedelta

class Rate:
    def __init__(self, format='value'):
        self.format = format

    def exchange_rates(self):
        r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        return r.json()['Valute']

    def make_format(self, currency):
        response = self.exchange_rates()
        if currency in response:
            if self.format == 'full':
                return response[currency]
            elif self.format == 'value':
                return response[currency]['Value']
            elif self.format == 'name_value':
                return f"{response[currency]['Name']} {response[currency]['Value']} руб."
        return 'Error'

    def eur(self, diff=False):
        response = self.make_format('EUR')
        if diff:
            previous_value = self.exchange_rates()['EUR']['Previous']
            current_value = response['Value'] if self.format == 'full' else response
            return current_value - previous_value
        return response

    def usd(self, diff=False):
        response = self.make_format('USD')
        if diff:
            previous_value = self.exchange_rates()['USD']['Previous']
            current_value = response['Value'] if self.format == 'full' else response
            return current_value - previous_value
        return response

    def get_currency_info(self, currency):
        return self.make_format(currency)

    def max_min_currency(self):
        rates = self.exchange_rates()
        max_currency = max(rates.values(), key=lambda x: x['Value'])
        min_currency = min(rates.values(), key=lambda x: x['Value'])
        return f"{max_currency['Name']} {max_currency['Value']} руб.", f"{min_currency['Name']} {min_currency['Value']} руб."

    def exchange_date_rates(self, date):
        formatted_date = datetime.strptime(date, '%Y-%m-%d').strftime('%Y/%m/%d')
        r = requests.get(f'https://www.cbr-xml-daily.ru/archive/{formatted_date}/daily_json.js')
        if r.status_code == 200:
            return r.json()['Valute']
        return 'Нет данных'

    def get_usd_rate_over_weeks(self, weeks=1):
        rates = {}
        for i in range(weeks):
            date = (datetime.now() - timedelta(days=i * 7)).strftime('%Y-%m-%d')
            rates[date] = self.exchange_date_rates(date).get('USD', {}).get('Value', 'Нет данных')
        return rates

    def get_currency_rate_over_weeks(self, currency, weeks=1):
        rates = {}
        for i in range(weeks):
            date = (datetime.now() - timedelta(days=i * 7)).strftime('%Y-%m-%d')
            exchange_data = self.exchange_date_rates(date)

            # Проверка, является ли exchange_data словарем
            if isinstance(exchange_data, dict):
                rates[date] = exchange_data.get(currency, {}).get('Value', 'Нет данных')
            else:
                rates[date] = exchange_data  # Здесь exchange_data - это строка 'Нет данных'

        return rates