#6개의 숫자를 뽑아 출력해주는 프로그램
import random

numbers = range(1, 46)
#마치 [1,2,3,...,45] 과 비슷하다

#alt + shift + 위 or 아래 방향키
#alt + 위 or 아래 방향키

lotto = random.sample(numbers, 6)   #sample() 중복되지않게 표본에서 지정 갯수만큼 표본 추출
print(sorted(lotto))    #자동정렬 sorted()
