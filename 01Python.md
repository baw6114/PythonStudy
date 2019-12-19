# Python

\- 프로그래밍이란 저장, 반복, 분기로 이루어진다

ex) 크리스마스 트리를 만든다

\> 저장 : 나무, 전구, 장식을 준비한다

\> 반복 : 나무가 예뻐질 때까지 나무를 장식한다

\> 분기 : 나무가 예쁜가?(len(tree)>20) 예-> 종료(크리스마스트리=나무) / 아니오-> 반복

반복 행위 중 이뤄지는 데이터 저장 : 나무 = 나무 + 장식

```python
Python 프로그래밍 Code
tree = '나무'
# len(tree) => 2
bulb = '전구'
deco = '장식'
while len(tree)<20 :
    tree = tree + bulb + deco; 
    #'나무전구장식' 계속해서 전구장식이 붙으며 반복
christmas_tree = tree;
print(christmas_tree);
```

