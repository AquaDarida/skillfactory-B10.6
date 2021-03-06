import requests
import json

VALUES = {'рубль': 'RUB',
          'евро': 'USD',
          'доллар': 'EUR',
          'юань': 'CNY',
          'иена': 'JPY',
          'вона': 'KRW',
          'фунт': 'GBP',
          'франк': 'CHF',
          'крона': 'CZK',
          'рупия': 'INR',
          'лира': 'TRY',
          'шекель': 'ILS',
          'рэнд': 'ZAR'}


class APIException(Exception):
    pass


class Exchange:
    @staticmethod
    def get_price(fValue: str, tValue: str, amount: str):
        try:
            fValue = VALUES[fValue]
            tValue = VALUES[tValue]
            amount = int(amount)

            if fValue == tValue:
                raise APIException('Нельзя конвертировать одинаковую валюту')

        except APIException as ex:
            return f'{ex}'
        except KeyError:
            return 'Данная валюта недоступна'
        except ValueError:
            return 'Количество валюты должен быть целым числом и больше нуля'

        request = requests.get(f'https://api.exchangeratesapi.io/latest?base={fValue}&symbols={tValue},{fValue}')
        return f'{amount * json.loads(request.content)["rates"][tValue]: .2f}'
