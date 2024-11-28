# 줄서는 방법

## 문제 설명

n명의 사람이 일렬로 줄을 서고 있습니다. n명의 사람들에게는 각각 1번부터 n번까지 번호가 매겨져 있습니다. n명이 사람을 줄을 서는 방법은 여러가지 방법이 있습니다. 예를 들어서 3명의 사람이 있다면 다음과 같이 6개의 방법이 있습니다.

- [1, 2, 3]
- [1, 3, 2]
- [2, 1, 3]
- [2, 3, 1]
- [3, 1, 2]
- [3, 2, 1]

사람의 수 n과, 자연수 k가 주어질 때, 사람을 나열 하는 방법을 사전 순으로 나열 했을 때, k번째 방법을 return하는 solution 함수를 완성해주세요.

## 제한 조건

- n은 20이하의 자연수 입니다.
- k는 n! 이하의 자연수 입니다.

## 입출력 예

|n|k|return|
|---|---|---|
|3|5|result|

---

## 문제 접근 (pseudocode)
1. n까지의 숫자 배열을 만든다.
2. n의 숫자로 만들 수 있는 배열의 종류는 n-1의 숫자로 만드는 배열에 n만큼 경우의 수가 곱해진다.
-> n개의 숫자가 맨앞에 오는 경우의 수의 묶음이 되고 그 뒤로는 (n-1)!만큼의 경우의 수가 각각온다.
3. k에 (n-1)!이 몇번 반복되는지를 확인하고 그 반복만큼 첫 번째 자리의 숫자값이 증가한다.
4. 재귀의 형태로 반복된다.
5. k가 1, 즉, 첫번째 경우의 수를 가져오는 것을 생각할 때, k를 그대로 주면 num_list에서 2번째 인덱스를 가져오게 된다. 첫번째 인덱스를 가져올 수 있도록 k-1로 이니셜해준다.

---

<br>

```python
def factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f


def solution(n, k):
    num_list = [num for num in range(1, n+1)]
    stack = list()
    k = k - 1
    while num_list:
        multi_num = k // factorial(n-1)
        stack.append(num_list[multi_num])
        del num_list[multi_num]
        k = k % factorial(n-1)
        n -= 1
    return stack
```