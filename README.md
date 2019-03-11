# Python_django-faker_pip_package
## pip package Faker
### 가짜 데이터를 생성하여 데이터가 많은 상황을 재현할 수 있음
## 적용방법
1. pip install
```
$ pip install faker 
```
2. import faker (/fake.py)
```python
from faker import Faker
```
3. 함수작성
```python
myfake = Faker()
# Farker의 메소드를 통해서 어떤 종류의 가짜데이터를 뽑아낼지 결정할 수 있음
# myfake.함수 이름 
print(myfake.name())
print(myfake.address())
print(myfake.text())
print(myfake.state())
print(myfake.sentence())
print(myfake.random_number())
```
4. 파일실행
```
$ python fake.py
```
- 한국어 데이터 생성
```python
myfake = Faker('ko_KR')
print(myfake.name())
print(myfake.address())
#print(myfake.text()) 사용불가
#print(myfake.state()) 사용불가
#print(myfake.sentence()) 사용불가
print(myfake.random_number())
```
- Fake 데이터 유지하기
```python
# Seed 파일 (코드를 실행 할때 같은 fake 데이터 표출)
myfake.seed(1) # seed number
print(myfake.name())
print(myfake.address())
print(myfake.text())
print(myfake.state())
print(myfake.sentence())
print(myfake.random_number())
```
- For 문을 활용하여 블로그에 가짜 데이터를 생성 할 수 있다.
