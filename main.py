import requests

url = 'https://www.4devs.com.br/ferramentas_online.php'
header = {
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.4devs.com.br',
    'referer': 'https://www.4devs.com.br/gerador_de_pessoas',
}

data = 'acao=gerar_pessoa&sexo=I&pontuacao=S&idade=0&cep_estado=&txt_qtde=1&cep_cidade='

solicitacao = requests.post(url, headers=header, data=data).json()

nome = (solicitacao['nome'])
idade = (solicitacao['idade'])
cpf = (solicitacao['cpf'])
dataNac = (solicitacao['data_nasc'])
sexo = (solicitacao['sexo'])

print(f"Nome: {nome} \nIdade: {idade}\nCPF: {cpf}\nIdade: {idade}\nData de nascimento: {dataNac}\nSexo: {sexo}")
