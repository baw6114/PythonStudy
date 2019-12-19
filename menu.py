#Random으로 오늘의 점심메뉴를 추천해주는 프로그램
import random

menu = ['새마을식당', '초원삼겹살', '멀캠20층', '홍콩반점', '순남시래기']

#dictionary
phone_book = {
    '새마을식당':'010-2536-2563',
    '초원삼겹살':'010-5987-8359',
    '멀캠20층':'010-3134-1347',
    '홍콩반점':'010-2361-1234',
    '순남시래기':'010-1236-3457'
}   #json파일 형식과 같아보이는데 같은방식일 것 같다
print(phone_book['새마을식당'])
lunch = random.choice(menu);
print(lunch);

#해당 식당의 전화번호를 같이 출력
print(phone_book[lunch])