# [Python django] Model&admin

멋쟁이 사자처럼 7기 운영진 교육 실습자료 입니다.

## Question?
- model에 어떻게 데이터를 담을 수 있을까?
- model의 데이터를 어떻게 view로 넘길 수 있을까?
- 데이터를 어떻게 화면에 띄울 수 있을까?

## Python - Class
- Class
    - 객체지향 프로그래밍의 기본 단위
    - 객체의 구조와 행동을 정의
    - 클래스는 메서드(method), 속성(property), 클래스 변수(class variable), 인스턴스 변수(instance variable), 초기자(initializer), 소멸자(destructor) 로 구성된다

## Model&admin
### Model
- 데이터를 만들고 데이터베이스를 다룰 수 있다.
    #데이터베이스는 장고와 별개
- 데이터의 처리 형식을 models.py에 Class로 정의할 수 있다.
    Class를 계속 호출하여 같은 형식의 데이터를 계속 생성할 수 있다.
- Django의 model.py를 변경하면 DB에 선언을 해야 한다.
```
$ python manage.py makemigrations  #마이그레이션 파일 생성
$ python manage.py migrate #db에 만든 변경내용 적용
```
### Admin
- 어드민 계정 생성
```
$ python  manage.py createsuperuser
```
- 계정 생성 후 admin.py 에 데이터 등록

## 요약
1. models.py 안에 어떤 종류의 데이터를 처리할지 Class로 선언
2. DB에 선언
    ```
    $ python manage.py makemigrations  #마이그레이션 파일 생성
    $ python manage.py migrate #db에 만든 변경내용 적용
    ```
3. admin 계정 생성, admin.py에 데이터 등록 
     ```
    $ python manage.py createsuperuser #어드민 계정 생성
    ```
- 데이터베이스에 어떤 데이터를 넣을지 정의하고, admin의 권한으로 데이터 생성	






