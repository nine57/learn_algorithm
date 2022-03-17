# 자릿수 더하기

## 문제 설명

자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.

## 제한 조건

N의 범위 : 100,000,000 이하의 자연수

## 입출력 예

|n|return|
|---|---|
|123|6|
|987|24|

---

## 문제 접근 (pseudocode)
1. input을 iterable한 string으로 변환
2. 자릿값을 순회하며 int로 변환하여 더해줌.

---

<br>

```python
def solution(n):
    return sum(map(int, str(n)))
```
> 통과 답안 : map으로 돌면서 나온 배열을 sum해준다.

<br>

---
<br>

### 다른 풀이

```python
def solution(n):
    if n < 10:
        return n
    return (n % 10) + solution(n // 10) 
```
> 재귀함수!
> (n % 10)으로 일의 자리를 누적해가며 함수를 재귀한다.
> 재귀 할 때 마다 n을 한자리씩 줄여가면서 호출한다.
> n이 일의 자리만 남았을 때 기저