# 올바른 괄호

## 문제 설명

괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 예를 들어<br>

"()()" 또는 "(())()" 는 올바른 괄호입니다.<br>
")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.<br>
'(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.

## 제한 조건

- 문자열 s의 길이 : 100,000 이하의 자연수
- 문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.

## 입출력 예

|s|answer|
|---|---|
|"()()"|true|
|"(())()"|true|
|")()("|false|
|"(()("|false|

---

## 문제 접근 (pseudocode)
1. 괄호를 열 때 카운트 업, 괄호를 닫을 때 카운트 다운
2. 카운트가 0일 때 닫는 괄호는 False
3. 문자열을 다 돌고 난 뒤 카운트가 0이 되지 않으면 False

---

<br>

```python
def solution(s):
    answer = True
    close_bracket = 0
    for c in s:
        if c == '(':
            close_bracket += 1
        else:
            if close_bracket == 0:
                answer = False
                break
            else:
                close_bracket -= 1

    if close_bracket != 0:
        answer = False

    return answer
```
