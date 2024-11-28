# N개의 최소공배수

## 문제 설명

두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다. 예를 들어 2와 7의 최소공배수는 14가 됩니다. 정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다. n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.

## 제한 조건

arr은 길이 1이상, 15이하인 배열입니다.
arr의 원소는 100 이하인 자연수입니다.

## 입출력 예

|arr|result|
|---|---|
|[2,6,8,14]|168|
|[1,2,3]|6|

---

## 문제 접근 (pseudocode)
1. 최소공배수 = 각각의 원소가 갖고있는 소수별로 최대의 값을 취한다.
2. 각각의 원소에 대해 소수로 나눠서 담아준다.
3. 소수의 사전에 소수의 최대 카운트로 담아준다.
4. 각 소수를 곱해서 출력

---

<br>

```python
def sieve(n):
    sieve = [True] * (n+1)
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            for j in range(i+i,n,i):
                sieve[j] = False
    return [i for i in range(2,n+1) if sieve[i]]

def solution(arr):
    n = max(arr)
    prime = sieve(n)
    
    arr_prime = {}

    for num in arr:
        for p_num in prime:
            if p_num > num:
                break
            cnt = 0
            while num%p_num==0:
                num /= p_num
                cnt += 1
            if p_num in arr_prime:
                if arr_prime[p_num] < cnt:
                    arr_prime[p_num] = cnt
            elif cnt != 0:
                arr_prime[p_num] = cnt

    answer = 1
    for prime in arr_prime:
        answer *= prime**arr_prime[prime]
    return answer
```
> 통과 답안 : 에라토스테네스의 체에서 소수를 구할 때, n까지만 구하면 max인 숫자 스스로가 소수일 경우에 오답이 발생한다.<br>
> 시간 복잡도가 상당히 나쁜 답으로 보인다.

<br>

---
<br>

### 다른 풀이
```python
from math import gcd

def solution(arr):      
    answer = arr[0]
    for n in arr:
        answer = (n * answer) // gcd(n, answer)
    return answer
```
> math 모듈의 gcd 메서드를 이용한 풀이<br>
> 두 수의 곱을 최대공약수(gcd)로 나누면 최소공배수가 된다는 점을 이용했다.<br>
> 배열을 순회하며 연속해서 최소공배수를 구하면 최종적으로 답을 출력할 수 있다.<br>
> 근데,,, 모듈 쓸거면 lcm()쓰면 바로 구할 수 있다...

### 다른 풀이 2 (병연님)
```python
def gcd(a, b):
    if a % b == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return a*b/gcd(a,b)

def solution(arr):
    while len(arr) >= 2:
        i = arr.pop()
        j = arr.pop()
        arr.append(lcm(i, j))
    return arr[0]
```
> gcd 메서드를 직접 구현했다. (유클리드 호제법이라고 한다.)<br>
> solution 함수에서 pop으로 뒤에서부터 빼는 이유는 앞의 인덱스부터 빼낼 시, O(n)의 시간 복잡도를 갖게 되기 때문<br>
> 뒤에서 빼줌으로 써 O(1)의 시간 복잡도로 처리 가능하다.<br>
> 단 이부분은 배열에서 두수를 뺐다가 다시 한개를 넣는 과정 없이, 변수를 선언해서 그 변수에 쌓아가는 식으로 개선 가능하다.