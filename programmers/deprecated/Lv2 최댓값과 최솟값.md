# title

## 문제 설명

문자열 s에는 공백으로 구분된 숫자들이 저장되어 있습니다.<br>
str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 "(최소값) (최대값)"형태의 문자열을 반환하는 함수, solution을 완성하세요.<br>
예를들어 s가 "1 2 3 4"라면 "1 4"를 리턴하고, "-1 -2 -3 -4"라면 "-4 -1"을 리턴하면 됩니다.

## 제한 조건

s에는 둘 이상의 정수가 공백으로 구분되어 있습니다.

## 입출력 예

|s|return|
|---|---|
|"1 2 3 4"|"1 4"|
|"-1 -2 -3 -4"|"-4 -1"|
|"-1 -1"|"-1 -1"|

---

## 문제 접근 (pseudocode)
1. 입력된 값을 공백 기준으로 분리해서 배열로 저장
2. 배열 내에서 최댓값과 최솟값을 찾아서 요구조건에 맞게 값을 리턴.

---

<br>

```python
def solution(s):
    number_list = list(map(int, s.split(' ')))
    answer_number = [str(min(number_list)), str(max(number_list))]
    answer = str(' '.join(answer_number))
    return answer
```
> 통과 답안 : join은 입력값을 str 타입으로만 받는다! 주의.

<br>

---
<br>

### 다른 풀이

```python
def solution(s):
    number_list = list(map(int, s.split(' ')))
    answer = str(min(number_list)) + ' ' + str(max(number_list))
    return answer
```
> 위의 답안에서 join을 쓰기위해서 list를 만들었는데, 실은 그냥 바로 원하는 결과값 형태로 반환하면 된다.