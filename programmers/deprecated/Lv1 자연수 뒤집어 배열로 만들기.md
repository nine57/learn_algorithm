# 자연수 뒤집어 배열로 만들기

## 문제 설명

자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

## 제한 조건

n은 10,000,000,000이하인 자연수입니다.

## 입출력 예

|n|return|
|---|---|
|12345|[5,4,3,2,1]|

---

## 문제 접근 (pseudocode)
1. input되는 값을 배열 형태로 변환
2. 변환된 배열을 역순으로 뒤집어준다.
3. 이때 input되는 값을 int이므로 iterable한 형태를 취한다.

---

<br>

```python
def solution(n):
    input_to_list = [int(i) for i in str(n)]
    answer = input_to_list[::-1]
    return answer
```
> 통과 답안 : 문제 그대로 input을 변환, 반전한 값을 출력한다.

<br>

---
<br>

### 다른 풀이

```python
def solution(n):
    return list(map(int, reversed(str(n))))
```
> reversed : Return a reverse iterator over the values of the given sequence. <br>
> map : Make an iterator that computes the function using arguments from each of the iterables. Stops when the shortest iterable is exhausted. <br>
> n을 string 형태로 바꿔 iterable하게 한 뒤, reversed로 뒤집어준다. <br>
> 이후 map으로 각각의 요소를 int로 다시 바꾼 값을 list에 담아준다.