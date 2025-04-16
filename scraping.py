import requests
from bs4 import BeautifulSoup

def pegar_horoscopo(signo):
    url = f"https://www.horoscopovirtual.com.br/horoscopo/{signo.lower()}"
    headers = {"User-Agent": "Mozilla/5.0"}

    resposta = requests.get(url, headers=headers)
    if resposta.status_code != 200:
        return {"erro": "Não foi possível acessar o site"}

    soup = BeautifulSoup(resposta.text, 'html.parser')

    paragrafo = soup.find('p', class_='text-pred')

    if paragrafo:
        # Remove o <a> interno ("Compartilhar")
        link = paragrafo.find('a')
        if link:
            link.decompose()

        texto = paragrafo.get_text(strip=True)
        return {"signo": signo, "horoscopo": texto}
    else:
        return {"erro": "Horóscopo não encontrado"}
