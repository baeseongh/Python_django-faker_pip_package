# Django Google Social Login API 구현

## 학습 목표
Allauth pip 패키지 사용하여 Google login api를 이용하여 소셜 로그인 기능을 구현한다.

## 1. 소셜 로그인

### 1.1 로그인 방식

#### 1.1.1 기존의 로그인 방식
- db.sqlite3에 유저 정보 저장
- DB와 DB를 다루는 로직이 한 공간에 존재
- Views.py
  - login(request), signup(request), logout(request)
#### 1.1.1 소셜 로그인
- DB와 DB를 다루는 로직이 다른 공간에 존재
- Request와 token 
***
### 1.2 기본 세팅(프로젝트 생성)
- 새로운 프로젝트를 생성하여 구현하였습니다. 기존 프로젝트에 구성하여도 무관합니다.
1. Project, app 생성
2. Settings.py app 등록
3. App/templates/home.html 생성
4. Urls.py 세팅
5. Views.py 세팅
6. models.py 세팅, 마이그레이트
7. Admin.py 세팅

***
### 1.3 pip 패키지

#### 1.3.1 pip 패키지 설치
```bash
$ pip install django-allauth
```

#### 1.3.2 pip 패키지 세팅
<code>project/settings.py</code>
```python
INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.sites',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'social.apps.SocialConfig', 
  # allauth
  'allauth',
  'allauth.account',
  'allauth.socialaccount',
  # provider 구글 페이스북 카톡 깃헙 (제공 업체)
  'allauth.socialaccount.providers.google',
] 
```
#### 1.3.4 provider 종류
```
## Provider
amazon, agave, auth0, basecamp, bitbucket, bitly, cern, coinbase, daum, discord, dropbox, evernote, facebook, filckr, github, gitlab, goole, huvic, instagram, kako, line, linkedin, naver, paypal, pinterest, reddit, shopify, slack, soundcloud, spotify, steam, trello, tumblr, twitch, twitter, vimeo, windowslive ...
```

#### 1.3.5 pip 패키지 세팅, 튜플 작성
<code>project/settings.py</code>
```python
AUTHENTICATION_BACKENDS = (
# Needed to login by username in django admin, regardless of 'allauth'
'django.contrib.auth.backends.ModelBackend',
# 'allauth' specific authentication methods, such as login by e-mail
'allauth.account.auth_backends.AuthenticationBackend',
)
 
SITE_ID = 1
 
LOGIN_REDIRECT_URL = '/'
```
***
### 1.4 프로젝트 세팅

#### 1.4.1 Url설정
  - project/urls.py
  - allauth의 url은 이미 설계되어 있기 때문에 가져다 쓰기만 하면 된다.
```python
from django.urls import path, include # app 밖의 url 이기 때문에 include

urlpatterns = [
	path('accounts/', include('allauth.urls')),
]
```

#### 1.4.2 마이그레이트
```shall
$ python manage.py migrate
```

#### 1.4.3 Admin 페이지
<code>localhost/admin/</code>

마이그레트 후 admin 페이지에 접속하면 많은 것들이 설치 되어 있다. 
1. 어드민 페이지의 site로 이동하여 example.com 을 클릭하여 Domain name과 Display name을 자신의 도메인 으로 수정 ex) 127.0.0.1:8000
2. Social applications로 이동하여 ADD SOCIAL APPLICATION 클릭 후 사용자 인증정보( 클라이언트 ID, 시크릿 키 등)기입 
- 사용 Api ex)Google api에서 인증정보를 받아올 수 있음 
	
#### 1.4.4 Google API 사용자 인증정보 생성
1. https://console.developers.google.com 이동
2. 프로젝트 생성
3. 사용자 인증정보(열쇠 모양) > 사용자 인증정보 만들기 > OAuth 클라이언트 ID 만들기 > 동의화면구성 > 애플리케이션 이름 입력 > 저장
4. 애플리케이션 유형 (웹) > 이름 입력
5. 승인된 자바스크립트 원본 (url 입력 ex) http://127.0.0.1:8000), 승인된 리디렉션 URI (동일 url 입력)
6. 생성

#### 1.4.5 생성된 인증정보 (클라이언트 ID, 스크릿 키) 어드민 페이지에 입력
<code>localhost/admin/</code>

#### 1.4.6 Admin 페이지
<code>localhost/admin/</code>

1. Add social application에서 sites 의 Available sites에 있는 디폴트 사이트를 Chosen sites에 추가
2. 저장
	
#### 1.4.7 Home.html 작성
<code>App/templates/home.html</code>
```django
{%load socialaccount%} <!--socialaccount로드-->
{%providers_media_js%}
<h1>Social login!</h1>
<!--로그인 판단-->
{% if user.is_authenticated%}
{{user.username}} 님이 로그인 중<br>
<!--pip패키지가 만들어준 로그아웃 url-->
<a href="/accounts/logout">로그아웃</a> 
{%else%}
<!--provider 'google' 사용-->
<a href="{%provider_login_url 'google'%}">구글 로그인</a><br>
<a href="/accounts/signup">회원가입</a><br>
{%endif%}
```
***
### Error 400이 뜨는 경우
1. Error페이지의 표출된 callback url을 복사한다.
2. Google api의 웹 애플리케이션의 > 클라이언트 ID > OAuth 클라이언트 ID 만들기 (credential 페이지)로 이동
3. 승인된 리디렉션 URI에 복사한 url을 추가한다.
	- http://127.0.0.1:8000/accounts/google/login/callback/
