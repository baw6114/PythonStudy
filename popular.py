import bs4
import requests

html = requests.get('https://www.naver.com/')
soup = bs4.BeautifulSoup(html.text, 'html.parser')

keywords = soup.select('span.ah_k')

#keywords 배열에서 keyword
#keywords = ['a', 'b', 'c']
#위의 keywords를 출력해보면 
#각각 a b c가 나옴을 알 수 있다
#for keyword in keywords:
#    print(keyword)

#배열[0:n] -> 배열의 0번째 인덱스부터 n-1번째 인덱스들의 요소를 가져와서 배열로 만든다
real_keywords = keywords[0:20]

#real_keywords에 있는 keyword들을 모두 뽑아낸다.
#그리고 해당 keyword배열을 설정한다
real_real_keywords = [keyword.text for keyword in real_keywords]
print(real_real_keywords)

#무엇이 1등인지 모르게 가나다 순 정렬
problem = sorted(real_real_keywords)
answer = input('당신이 엽력한 답 :')

if answer == real_real_keywords[0]:
    print('정답')
else:
    print('오답')

#[]속 문법 공부
#numbers = [i for i in range(0,101)]
#print(numbers)

#numbers = []
#for i in range(0,101):
#    numbers.append(i)
#print(numbers)
