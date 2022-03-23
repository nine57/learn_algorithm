# 행렬의 곱셈

## 문제 설명

2차원 행렬 arr1과 arr2를 입력받아, arr1에 arr2를 곱한 결과를 반환하는 함수, solution을 완성해주세요.

## 제한 조건

- 행렬 arr1, arr2의 행과 열의 길이는 2 이상 100 이하입니다.
- 행렬 arr1, arr2의 원소는 -10 이상 20 이하인 자연수입니다.
- 곱할 수 있는 배열만 주어집니다.

## 입출력 예

|arr1|arr2|return|
|---|---|---|
|[[1, 4], [3, 2], [4, 1]]|[[3, 3], [3, 3]]|[[15, 15], [15, 15], [15, 15]]|
|[[2, 3, 2], [4, 2, 4], [3, 1, 4]]|[[5, 4, 3], [2, 4, 1], [3, 1, 1]]|[[22, 22, 11], [36, 28, 18], [29, 20, 14]]|

---

## 문제 접근 (pseudocode)
1. a = 0 ~ len(arr1)-1 만큼 이동
2. b = 0 ~ len(arr2[0])-1 만큼 이동, 0 ~ len(arr1[0])-1 만큼 배열 곱
3. 곱이 가능한 행렬이 주어지기 때문에 b는 arr1, arr2 에서 같은 이동 좌표로 사용 가능하다.
4. c =  / d = 0 ~ len(arr2)-1 만큼 배열 곱
5. 현재 좌표의 계산 값을 sum_value에 누적하고 끝 좌표에서 answer 배열에 삽입 후 0으로 초기화

---

<br>

```python
def solution(arr1, arr2):
    answer = [[] for _ in range(len(arr1))]
    a, b, c, sum_value = 0, 0, 0, 0

    while True:
        sum_value += arr1[a][b]*arr2[b][c]
        if b < len(arr1[0])-1:
            b += 1

        elif c < len(arr2[0])-1:
            answer[a].append(sum_value)
            c += 1
            b, sum_value = 0, 0

        elif a < len(arr1)-1:
            answer[a].append(sum_value)
            a += 1
            b, c, sum_value = 0, 0, 0

        else:
            answer[a].append(sum_value)
            break

    return answer
```
> 통과 답안 : 정확도는 100%지만 일부 테스트에서 효율성이 극단적으로 낮아진다.<br>
> 원인 확인 요!

<br>

---
<br>

### 다른 풀이 (병연님)

```python
def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer
```
> 삼중 for문 구조, 내 통과 답안보다 빠르다...<br>
> 