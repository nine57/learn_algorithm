# 피보나치 수

## 문제 설명

피보나치 수는 F(0) = 0, F(1) = 1일 때, 1 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 수 입니다.<br>
예를들어<br>
F(2) = F(0) + F(1) = 0 + 1 = 1<br>
F(3) = F(1) + F(2) = 1 + 1 = 2<br>
F(4) = F(2) + F(3) = 1 + 2 = 3<br>
F(5) = F(3) + F(4) = 2 + 3 = 5<br>
와 같이 이어집니다.<br>
2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.

## 제한 조건

n은 2 이상 100,000 이하인 자연수입니다.

## 입출력 예

|n|return|
|---|---|
|3|2|
|5|5|

## 입출력 예 설명
피보나치수는 0번째부터 0, 1, 1, 2, 3, 5, ... 와 같이 이어집니다.

---

## 문제 접근 (pseudocode)
1. n번째의 피보나치 수를 구한다.
2. 피보나치 수를 1234567로 나눈 나머지를 리턴한다.

---

<br>

```python
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-2) + fib(n-1)


def solution(n):
    fib_num = fib(n)
    answer = fib_num % 1234567
    return answer
```
> 최초 답안 :
> ### 문제 접근
> 1. n번째의 피보나치 수를 구한다.
> 2. 피보나치 수를 1234567로 나눈 나머지를 리턴한다.<br>
> 
> -> 시간초과와 Recursion Error(런타임 에러)가 발생한다.

<br>

```python
def fib(n):
    fib_num = 1
    tmp = 0
    for _ in range(n-1):
        fib_num, tmp = fib_num+tmp, fib_num
    return fib_num


def solution(n):
    fib_num = fib(n)
    answer = fib_num % 1234567
    return answer
```
> 통과 답안 : 코드 효율성 문제로 인해서 재귀함수는 사용 불가. <br>
> 반복문으로 피보나치 수를 계산<br>
> 재귀함수로 피보나치 수를 구할 경우 20번째만 넘어가도 시간이 100배 가량 차이가 발생한다.