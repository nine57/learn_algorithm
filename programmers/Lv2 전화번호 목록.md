# 전화번호 목록

## 문제 설명
전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.<br>
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.<br>

- 구조대 : 119
- 박준영 : 97 674 223
- 지영석 : 11 9552 4421

전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

## 제한 조건
- phone_book의 길이는 1 이상 1,000,000 이하입니다.
    - 각 전화번호의 길이는 1 이상 20 이하입니다.
    - 같은 전화번호가 중복해서 들어있지 않습니다.


## 입출력 예

|phone_book|return|
|---|---|
|["119", "97674223", "1195524421"]|false|
|["123","456","789"]|true|
|["12","123","1235","567","88"]|false|

---

## 문제 접근 (pseudocode)
1. for 문으로 list를 전부 순회하는 것은 너무 비효율적.
2. 문제를 단순화할 것.
3. 해결책 1 : 2중 Loop을 통해 서로가 서로의 접두어인지를 전부 확인하는 방법<br>
해결책 2 : Sorting 후 1중 Loop을 통해 앞의 번호가 뒷 번호의 접두어인지 확인하는 방법<br>
해결책 3 : 해시를 통해 접두어가 존재하는지를 확인하는 방법<br>

---

<br>

```python
def solution(phone_book):
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = True

    for phone_number in phone_book:
        checker = ''
        for number in phone_number:
            checker += number
            if checker in hash_map and checker != phone_number:
                return False
    return True
```
> 통과 답안 : 주어진 배열을 순회하면서 hash_map에 값을 True로 정의<br>
> 다시 배열을 재순회하면서 각각의 숫자의 길이만큼 반복해서 hash_map을 체크

<br>

---
<br>

### 다른 풀이

```python
def solution(phone_book):
    phoneBook.sort()
    for i in range(len(phoneBook) - 1):
        if phoneBook[i+1].startswith(phoneBook[i]):
            return False
    return True
```
> hash를 사용하지 않고, 배열을 정렬한 뒤에 바로 앞뒤의 숫자를 비교하는 방법으로도 탐색이 가능하다.