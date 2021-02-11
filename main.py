from bs4 import BeautifulSoup
import requests


url = 'https://www.reddit.com/r/ClashRoyale/'

global headers


headers = {
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, 'lxml')


for item in soup.select('.Post'):
    try:
        print('----------------------------------------')
        print(item.select('._eYtD2XCVieq6emjKBH3m')[0].get_text())
        print(item.select('.FHCV02u6Cp2zYL0fhQPsO')[0].get_text())
        print(item.select('._1E9mcoVn4MYnuBQSVDt1gC')[0].get_text())
        print(item.select('._3jOxDPIQ0KaOWpzvSQo-1s')[0].get_text())
       # print(item.select('.')[0]['href'])	
    #except Exception as e:
        
