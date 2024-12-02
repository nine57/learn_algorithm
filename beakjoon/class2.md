### [11650](https://www.acmicpc.net/problem/11650)
<details>
<summary>풀이</summary>

```python

```
</details>

---

### [10814](https://www.acmicpc.net/problem/10814)
<details>
<summary>풀이</summary>

```python
n = int(input())
D = {i: [] for i in range(1, 201)}
for i in range(n):
    inp = input().split()
    age = int(inp[0])
    name = inp[1]
    D[age].append(name)
for idx in range(1, 201):
    if names := D[idx]:
        for name in names:
            print(idx, name)
    else:
        continue

```
</details>

---

### [1676](https://www.acmicpc.net/problem/1676)
<details>
<summary>풀이</summary>

```python
n = int(input())
cnt_2, cnt_5 = 0, 0
for n in range(1, n+1):
    while True:
        if n % 2 == 0:
            cnt_2 += 1
            n //= 2
        else:
            break
    while True:
        if n % 5 == 0:
            cnt_5 += 1
            n //= 5
        else:
            break
print(min(cnt_2, cnt_5))
```
</details>

---

### [1436](https://www.acmicpc.net/problem/1436)
<details>
<summary>풀이</summary>

```python
n = int(input())
cnt = 0
num = 666
while True:
    if "666" in str(num):
        cnt += 1
    if cnt == n:
        break
    num += 1
print(num)
```
</details>

---

### [1181](https://www.acmicpc.net/problem/1181)
<details>
<summary>풀이</summary>

```python
words = set()
for _ in range(int(input())):
    words.add(input())
for i in sorted(list(words), key=lambda x: (len(x), x)):
    print(i)

```
</details>

---

### [10989](https://www.acmicpc.net/problem/10989)
<details>
<summary>풀이</summary>

```python
import sys
inp = sys.stdin.readline

n = int(inp())
cnt = [0] * 10001
for _ in range(n):
    num = int(inp())
    cnt[num] += 1

for i in range(10001):
    if cnt[i] != 0:
        for j in range(cnt[i]):
            print(i)
```
</details>

---

### [28702](https://www.acmicpc.net/problem/28702)
<details>
<summary>풀이</summary>

```python
def fizzbuzz(v):
    if v % 15 == 0:
        print('FizzBuzz')
    elif v % 3 == 0:
        print('Fizz')
    elif v % 5 == 0:
        print('Buzz')
    else:
        print(v)

inputs = [input().strip() for _ in range(3)]
answer_value = ''
for idx, value in enumerate(inputs):
    if value.isdigit():
        answer_value = int(value) + (3-idx)
        break
fizzbuzz(answer_value)
```
</details>

---

### [11050](https://www.acmicpc.net/problem/11050)
<details>
<summary>풀이</summary>

```python

```
</details>

---

### [2609](https://www.acmicpc.net/problem/2609)
<details>
<summary>풀이</summary>

```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

m, n = map(int, input().split())
m, n = max(m, n), min(m, n)

g = gcd(m, n)
print(g)
print(int(m * n / g))
```
</details>

---

### [1259](https://www.acmicpc.net/problem/1259)
<details>
<summary>풀이</summary>

```python
while True:
    case = input()
    if case == "0":
        break

    l = len(case)
    mid = l // 2
    front = case[:mid]
    if l % 2 == 1:
        back = case[:mid:-1]
    else:
        back = case[:mid-1:-1]
    if front == back:
        print("yes")
    else:
        print("no")
```
</details>

---

### [15829](https://www.acmicpc.net/problem/15829)
<details>
<summary>풀이</summary>

```python
import string

L = int(input())
c_map = {c: idx + 1 for idx, c in enumerate(string.ascii_lowercase)}
trans = [c_map[c] for c in input()]
r = 31
M = 1234567891
s = 0
for idx, num in enumerate(trans):
    s += num * (r**idx)
print(s % M)
```
</details>

---

### [30802](https://www.acmicpc.net/problem/30802)
<details>
<summary>풀이</summary>

```python
import sys
N = int(sys.stdin.readline())
sizes = map(int, sys.stdin.readline().split())
t_pack, s_pack = map(int, sys.stdin.readline().split())
ts = 0
for count_per_size in sizes:
    ts += count_per_size // t_pack
    ts += 1 if count_per_size % t_pack else 0
print(ts)
print(N // s_pack, N % s_pack)
```
</details>

---

### [4153](https://www.acmicpc.net/problem/4153)
<details>
<summary>풀이</summary>

```python
END = "0 0 0"
while True:
    case = input()
    if case == END:
        break

    a, b, c = map(int, case.split())
    diagonal = max(a, b ,c)
    rest = [a, b, c]
    rest.remove(diagonal)
    if rest[0]**2 + rest[1]**2 == diagonal**2:
        print("right")
    else:
        print("wrong")
```
</details>

---