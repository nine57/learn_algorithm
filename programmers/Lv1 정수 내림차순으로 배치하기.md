# 정수 내림차순으로 배치하기

## 문제 설명

함수 solution은 정수 n을 매개변수로 입력받습니다. n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 예를들어 n이 118372면 873211을 리턴하면 됩니다.

## 제한 조건

n은 1이상 8000000000 이하인 자연수입니다.

## 입출력 예

|n|return|
|----|----|
|118372|873211|

---

## 문제 접근 (pseudocode)
1. 반복문으로 처음부터 끝까지 돌면서 앞의 숫자와 비교한다
2. 비교해서 앞의 숫자가 더 크다면 위치를 바꿔준다.
3. 바꿔주면서 변경 체크값을 1로 바꿔준다.
4. 마지막 번호까지 반복한다.
5. 변경 체크값이 0이면 아웃하고 리턴한다.

---

<br>

```python
def recursion(number_length, number_list):
    check = False
    for idx in range(1, number_length):
        if number_list[idx] > number_list[idx-1]:
            number_list[idx], number_list[idx-1] = number_list[idx-1], number_list[idx]
            check = True
    
    if not check:
        result = int(''.join(map(str, number_list)))
        return result

    return recursion(number_length, number_list)

def solution(n):
    string_number = str(n)
    number_list = [int(number) for number in string_number]
    number_length = len(number_list)

    answer = recursion(number_length, number_list)
    return answer
```
> 1번째 제출 답안 :<br>
> Runtime error 발생으로 실패 (@ Test. 2, 3, 11)

<br>

```python
def recursion(number_length, number_list):
    check = False
    for idx in range(1, number_length):
        if number_list[idx] > number_list[idx-1]:
            number_list[idx], number_list[idx-1] = number_list[idx-1], number_list[idx]
            check = True
    
    if not check:
        result = int(''.join(map(str, number_list)))
        return result

    return recursion(number_length, number_list)

def solution(n):
    string_number = str(int(n))
    number_list = [int(number) for number in string_number]
    number_length = len(number_list)

    answer = recursion(number_length, number_list)
    return answer
```
> 통과 답안 :<br>
> solution 함수로 들어오는 input을 int(n)으로 변환하면 Runtime error가 뜨지 않는다...<br>
> 분명 문제에서 'n은 자연수이다'라고 했으나, 문자열도 숫자도 아닌 다른 형태의 값이 들어오는 것으로 추정된다.<br>
> 추가 확인 필요...

<br>

---
<br>

### 다른 풀이

```python
def solution(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))
```
> 마찬가지로 n의 input값을 int()로 한번 변환해줘야 정답이 된다.(미반영)<br>
> sort 메서드에 reverse를 줘서 손쉽게 해결할 수 있는 문제.