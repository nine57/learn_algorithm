# 주차 요금 계산

## 문제 설명

https://programmers.co.kr/learn/courses/30/lessons/92341?language=python3

---

## 문제 접근 (pseudocode)
1. 차는 여러번 드나들 수 있다.
2. 누적된 시간으로 기본 시간보다 작으면 기본 요금을 리턴한다
3. 초과한 시간만큼을 단위시간 단위로 요금을 청구한다. (올림)
4. 차량이 In이면 객체에 넣고, Out이면 객체에서 나온다. ->나올때 0을준다?
5. 마지막까지 남아있으면 23:59를 준다. (1439)

---

<br>

```python
def solution(fees, records):
    in_out_checker = {}
    time_accum = {}
    answer = []
    
    for record in records:
        time_str, number, in_out = record.split(' ')
        hour, minute = map(int,time_str.split(':'))
        time = hour*60 + minute
        
        if number in in_out_checker:
            if in_out=='IN':
                in_out_checker[number]=time
            else:
                time_accum[number] += (time-in_out_checker[number])
                in_out_checker[number]=-1
        else:
            in_out_checker[number]=time
            time_accum[number]=0
            
    for number in in_out_checker:
        if in_out_checker[number] != -1:
            time_accum[number] += (1439-in_out_checker[number])
            
    sorted_number = sorted(time_accum.keys())
    for number in sorted_number:
        fee=0
        if time_accum[number] <= fees[0]:
            fee=fees[1]
        else:
            time_for_pay = time_accum[number]-fees[0]
            if time_for_pay % fees[2]==0:
                fee=fees[1]+(time_for_pay//fees[2])*fees[3]
            else:
                fee=fees[1]+((time_for_pay//fees[2])+1)*fees[3]
        answer.append(fee)

    return answer
```
> 통과 답안 : 입력되는 정보들을 파싱해서 원하는 값으로 변환해서 사용<br>
> 최종 요금을 구하는 for문이 더 간단하 로직으로 구현될 수 있을 것으로 보이는데...

<br>

---
<br>

### 다른 풀이

```python
from collections import defaultdict
from math import ceil

class Parking:
    def __init__(self, fees):
        self.fees = fees
        self.in_flag = False
        self.in_time = 0
        self.total = 0

    def update(self, t, inout):
        self.in_flag = True if inout=='IN' else False
        if self.in_flag:  self.in_time = str2int(t)
        else:             self.total  += (str2int(t)-self.in_time)

    def calc_fee(self):
        if self.in_flag: self.update('23:59', 'out')
        add_t = self.total - self.fees[0]
        return self.fees[1] + ceil(add_t/self.fees[2]) * self.fees[3] if add_t >= 0 else self.fees[1]

def str2int(string):
    return int(string[:2])*60 + int(string[3:])

def solution(fees, records):
    recordsDict = defaultdict(lambda:Parking(fees))
    for rcd in records:
        t, car, inout = rcd.split()
        recordsDict[car].update(t, inout)
    return [v.calc_fee() for k, v in sorted(recordsDict.items())]
```
> 클래스를 활용한 문제풀이.. 클래스 활용에 익숙해지자.