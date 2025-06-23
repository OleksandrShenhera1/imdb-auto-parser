import requests
from bs4 import BeautifulSoup


def showIp():

    link = "https://api.ipify.org"

    response = requests.get(link).text

    soup = BeautifulSoup(response, 'lxml')

    requestIp = soup.find()

    print(f"Ip: {requestIp.text}")

