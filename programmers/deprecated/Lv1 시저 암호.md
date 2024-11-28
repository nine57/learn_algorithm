# 시저 암호

## 문제 설명

어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다. 예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다. "z"는 1만큼 밀면 "a"가 됩니다. 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.


## 제한 조건

- 공백은 아무리 밀어도 공백입니다.
- s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있습니다.
- s의 길이는 8000이하입니다.
- n은 1 이상, 25이하인 자연수입니다.

## 입출력 예

|s|n|return|
|---|---|---|
|"AB"|1|"BC"|
|"z"|1|"a"|
|"a B z"|4|"e F d"|
	
---

## 문제 접근 (pseudocode)
1. Input된 s를 각 자리값마다 ASCII로 변환
2. 공백은 값 shift 없이 문자로 변환 후 정답변수에 삽입
3. 그 외에는 소문자와 대문자를 구분해서 순환 조건 부여
4. 문자로 다시 변환해서 정답변수에 삽입.

---

<br>

```python
def solution(s, n):
    answer = ''
    for char in s:
        if char == ' ':
            answer += char
        else:
            asc = ord(char)
            plus_asc = asc + n
            if asc < 91 and plus_asc > 90:
                plus_asc -= 26
            elif asc > 96 and plus_asc > 122:
                plus_asc -= 26
            answer += chr(plus_asc)

    return answer
```
> 통과 답안 : asc의 대소관계를 구분하는 부분에서 x in range(a,b)의 형태로 줄 수 도 있지만, 이렇게 되면 시간 복잡도 측면에서 불리해진다.

<br>

---
<br>

### 다른 풀이

```python
def solution(s, n):
    answer = ''
    for char in s:
        asc = ord(char)
        plus_asc = asc + n
        if asc == 32:
            pass
        elif asc < 91 and plus_asc > 90:
            asc = plus_asc - 26
        elif plus_asc > 122:
            asc = plus_asc - 26
        else:
            asc = plus_asc
        answer += chr(asc)

    return answer
```
> 위와 동일한 로직이지만, 공백을 구분없이 아스키코드 변환한 뒤, 그 코드 번호를 패싱한다.<br>
> 이렇되면 if문 안에서 if문이 하나 더 돌아가는게 아니라, if문 하나에서 끝낼 수 있다!