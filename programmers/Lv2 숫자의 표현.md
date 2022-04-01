# 숫자의 표현

## 문제 설명

Finn은 요즘 수학공부에 빠져 있습니다.<br>
수학 공부를 하던 Finn은 자연수 n을 연속한 자연수들로 표현 하는 방법이 여러개라는 사실을 알게 되었습니다.<br>
예를들어 15는 다음과 같이 4가지로 표현 할 수 있습니다.<br>

1 + 2 + 3 + 4 + 5 = 15<br>
4 + 5 + 6 = 15<br>
7 + 8 = 15<br>
15 = 15<br>

자연수 n이 매개변수로 주어질 때, 연속된 자연수들로 n을 표현하는 방법의 수를 return하는 solution를 완성해주세요.

## 제한 조건

- n은 10,000 이하의 자연수 입니다.

## 입출력 예

|n|return|
|---|---|
|15|4|

---

## 문제 접근 (pseudocode)
1. 투 포인터로 해결해보자.
2. 대신 리스트를 따로 만드는게 아니라 가상의 리스트로 생각!

---

<br>

```python
def solution(n):
    answer = 0
    lt = 1
    rt = 1
    sum_number = 1

    while True:
        if sum_number < n:
            rt += 1
            if rt > n:
                break
            sum_number += rt
        elif sum_number > n:
            sum_number -= lt
            lt += 1
        else:
            answer += 1
            rt += 1
            if rt > n:
                break
            sum_number += rt

    return answer
```
> 통과 답안 : 정확도, 효율 OK, but while문 탈출 조건을 다시 걸어두는게 좋을 것 같다.

<br>

---
<br>

### 다른 풀이

```python
def solution(n):
    answer = 0
    lt = 1
    rt = 1
    sum_number = 1

    while rt<= n:
        if sum_number < n:
            rt += 1
            sum_number += rt
        elif sum_number > n:
            sum_number -= lt
            lt += 1
        else:
            answer += 1
            rt += 1
            sum_number += rt

    return answer
```
> 탈출조건을 while문 시작에 명시해줬다.<br>
> 특정 케이스는 시간이 더 오래 걸렸지만, if문 확인이 줄어서 앞의 정답보다는 더 효율적인 코드로 보인다.

<br>

### 다른 풀이2

```python
def solution(num):
    answer = 0
    for i in range(1, num + 1):
        s = 0
        while s < num:
            s += i
            i += 1
        if s == num:
            answer += 1

    return answer
```
> 코드는 간단해 보이나, 효율성 테스트에서 더 나쁜 결과가 나온다.