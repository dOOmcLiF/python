import requests

class Rate:
    def __init__(self, format='value'):
        self.format = format

    def exchange_rates(self):
        r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        return r.json()['Valute']

    def make_format(self, currency, diff=False):
        response = self.exchange_rates()

        if currency in response:
            if diff:
                previous_value = response[currency]['Previous']
                current_value = response[currency]['Value']
                return current_value - previous_value

            if self.format == 'full':
                return response[currency]

            if self.format == 'value':
                return response[currency]['Value']

            if self.format == 'name_value':
                return f"{response[currency]['Name']} {response[currency]['Value']} руб."

        return 'Error'

    def eur(self, diff=False):
        return self.make_format('EUR')

    def usd(self, diff=False):
        return self.make_format('USD')

    def currency_info(self, currency_code):
        return self.make_format(currency_code, diff=False)