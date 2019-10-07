import requests

cabecalho = {'User-agent': 'Windows 12',
             'Referer': 'https://google.com'}


meus_cookies = {'ultima_visita': '10-10-2020'}

dados = {'username': 'deborah',
        'password': '1234'}


texto = None
try:
    requisicao = requests.post('https://putsreq.com/oaKxLMN0j2xtotgKkiRV', headers=cabecalho, cookies= meus_cookies,
                               data=dados)
    texto = requisicao.text
    print(requisicao.text)
except Exception as e:
    print('Erro na requisicao.')

print(requisicao.text)
