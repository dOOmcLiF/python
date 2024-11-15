import requests
from datetime import datetime, timedelta


class Rate:
    def __init__(self, format='value'):
        self.format = format
        self.base_url = 'https://www.cbr-xml-daily.ru'

    def exchange_rates(self):
        try:
            r = requests.get(f'{self.base_url}/daily_json.js')
            return r.json()['Valute']
        except:
            return None

    def exchange_date_rates(self, date):
        try:
            date_str = date.strftime("%Y/%m/%d")
            r = requests.get(f'{self.base_url}/archive/{date_str}/daily_json.js')
            return r.json()['Valute']
        except:
            return None

    def make_format(self, currency):
        response = self.exchange_rates()
        if response and currency in response:
            if self.format == 'full':
                return response[currency]
            elif self.format == 'value':
                return response[currency]['Value']
            elif self.format == 'name':
                return f"{response[currency]['Name']} {response[currency]['Value']} руб."

        return 'Error'

    def eur(self, diff=False):
        response = self.exchange_rates()
        if response and 'EUR' in response:
            if diff:
                return response['EUR']['Value'] - response['EUR']['Previous']
            return self.make_format('EUR')
        return 'Error'

    def usd(self, diff=False):
        response = self.exchange_rates()
        if response and 'USD' in response:
            if diff:
                return response['USD']['Value'] - response['USD']['Previous']
            return self.make_format('USD')
        return 'Error'

    def get_currency(self, code):
        return self.make_format(code)

    def get_max_currency(self):
        response = self.exchange_rates()
        if response:
            max_currency = max(response.items(), key=lambda x: x[1]['Value'])
            return f"{max_currency[1]['Name']} {max_currency[1]['Value']} руб."
        return 'Error'

    def get_min_currency(self):
        response = self.exchange_rates()
        if response:
            min_currency = min(response.items(), key=lambda x: x[1]['Value'])
            return f"{min_currency[1]['Name']} {min_currency[1]['Value']} руб."
        return 'Error'

    def get_usd_history(self, weeks=1):
        history = {}
        current_date = datetime.now()

        for i in range(weeks * 7):
            date = current_date - timedelta(days=i)
            rates = self.exchange_date_rates(date)

            if rates and 'USD' in rates:
                history[date.strftime("%Y-%m-%d")] = rates['USD']['Value']
            else:
                history[date.strftime("%Y-%m-%d")] = 'Нет данных'

        return history

    def get_currency_history(self, code, weeks=1):
        history = {}
        current_date = datetime.now()

        for i in range(weeks * 7):
            date = current_date - timedelta(days=i)
            rates = self.exchange_date_rates(date)

            if rates and code in rates:
                history[date.strftime("%Y-%m-%d")] = rates[code]['Value']
            else:
                history[date.strftime("%Y-%m-%d")] = 'Нет данных'

        return history