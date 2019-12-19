import bs4
import requests

html = requests.get('https://finance.naver.com/marketindex/?tabSel=exchange#tab_section')

soup = bs4.BeautifulSoup(html.text, 'html.parser')

dollar = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value')

print(f'원/달러 환율 : {dollar.text}')