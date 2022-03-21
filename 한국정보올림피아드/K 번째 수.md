# K 번째 수

## 문제
N개의 숫자로 이루어진 숫자열이 주어지면 해당 숫자열중에서 s번째부터 e번째 까지의 수를 오름 차순 정렬했을 때 k번째로 나타나는 숫자를 출력하는 프로그램을 작성하세요.

## 입력
첫 번째 줄에 테스트 케이스 T(1<=T<=10)이 주어집니다.<br>
각 케이스별<br>
첫 번째 줄은 자연수 N(5<=N<=500), s, e, k가 차례로 주어진다.<br>
두 번째 줄에 N개의 숫자가 차례로 주어진다.

## 출력
각 케이스별 k번째 수를 아래 출력예제와 같이 출력하세요.

## 입출력 예
### 예제 입력1
```
2
6 2 5 3
5 2 7 3 8 9
15 3 10 3
4 15 8 16 6 6 17 3 10 11 18 7 14 7 15
```
### 예제 출력1
```
7
6
```

## 문제 접근
1. 주어진 대상 숫자열을 리스트에 넣는다.
2. s ~ e 까지만 슬라이싱 후 오름차순 정렬한다. (인덱스 번호 주의)
3. k 번째 숫자를 출력 (인덱스 번호 주의)

--- 

## 제출 답안

```python
def func(num_list, s, e, k):
    ordered_list = num_list[s-1:e]
    ordered_list.sort()
    answer = ordered_list[k-1]
    return answer


T = int(input())

for _ in range(T):
    N, s, e, k = map(int, input().split())
    num_list = list(map(int, input().split()))
    print(func(num_list, s, e, k))
```