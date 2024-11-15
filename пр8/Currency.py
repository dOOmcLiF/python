import requests
from datetime import datetime, timedelta

class Rate:
    def __init__(self, format='value'):
        self.format = format

    def exchange_rates(self):
        """
        Возвращает ответ сервиса с информацией о валютах в виде:
        {
            'AMD': {
                'CharCode': 'AMD',
                'ID': 'R01060',
                'Name': 'Армянских драмов',
                'Nominal': 100,
                'NumCode': '051',
                'Previous': 14.103,
                'Value': 14.0879
            },
            ...
        }
        """
        r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        return r.json()['Valute']

    def make_format(self, currency):
        """
        Возвращает информацию о валюте currency в двух вариантах:
        - полная информация о валюте при self.format = 'full':
        Rate('full').make_format('EUR')
        {
            'CharCode': 'EUR',
            'ID': 'R01239',
            'Name': 'Евро',
            'Nominal': 1,
            'NumCode': '978',
            'Previous': 79.6765,
            'Value': 79.4966
        }
        Rate('value').make_format('EUR')
        79.4966
        Rate('name_value').make_format('EUR')
        'Евро 79.4966 руб.'
        """
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
        """Возвращает курс евро на сегодня в формате self.format"""
        response = self.make_format('EUR')
        if diff:
            previous_value = self.exchange_rates()['EUR']['Previous']
            current_value = response['Value'] if self.format == 'full' else response
            return current_value - previous_value
        return response

    def usd(self, diff=False):
        """Возвращает курс доллара на сегодня в формате self.format"""
        response = self.make_format('USD')
        if diff:
            previous_value = self.exchange_rates()['USD']['Previous']
            current_value = response['Value'] if self.format == 'full' else response
            return current_value - previous_value
        return response

    def get_currency_info(self, currency):
        """Возвращает информацию о произвольной валюте"""
        return self.make_format(currency)

    def max_min_currency(self):
        """Возвращает валюту с максимальной и минимальной стоимостью"""
        rates = self.exchange_rates()
        max_currency = max(rates.values(), key=lambda x: x['Value'])
        min_currency = min(rates.values(), key=lambda x: x['Value'])
        return f"{max_currency['Name']} {max_currency['Value']} руб.", f"{min_currency['Name']} {min_currency['Value']} руб."

    def exchange_date_rates(self, date):
        """Получает курсы валют на указанную дату в формате 'YYYY-MM-DD'"""
        formatted_date = datetime.strptime(date, '%Y-%m-%d').strftime('%Y/%m/%d')
        r = requests.get(f'https://www.cbr-xml-daily.ru/archive/{formatted_date}/daily_json.js')
        if r.status_code == 200:
            return r.json()['Valute']
        return 'Нет данных'

    def get_usd_rate_over_weeks(self, weeks=1):
        """Получает курс доллара за указанное количество недель"""
        rates = {}
        for i in range(weeks):
            date = (datetime.now() - timedelta(days=i * 7)).strftime('%Y-%m-%d')
            rates[date] = self.exchange_date_rates(date).get('USD', {}).get('Value', 'Нет данных')
        return rates

    def get_currency_rate_over_weeks(self, currency, weeks=1):
        """Получает курс произвольной валюты за указанное количество недель"""
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