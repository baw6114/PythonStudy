#명단에서 이름을 뽑아서 영어소개와 한글소개
import random

name = ['홍길동', '희동이', '둘리']
eng_name = {
    '홍길동':'hong',
    '희동이':'dong',
    '둘리':'twolee'
}

지목된사람 = random.choice(name)
지목된영어이름 = eng_name[지목된사람]

intro = '저는 ' + 지목된사람 + '입니다' + ' My name is ' + 지목된영어이름
intro2 = '저는 {}입니다 My name is {}'.format(지목된사람,지목된영어이름)
intro3 = f'저는 {지목된사람}입니다 My name is {지목된영어이름}'
#.format해당하는 곳에 존재하는 변수들을 입력해준다
#f'{변수명}{변수명}'이와 같이 어떤 위치에 어떤 변수가 들어가는지 쉽게 알아볼 수 있는 형식도 존재
print(intro)
print(intro2)
print(intro3)