# Map API Django Naver Maps API 구현
## 학습 목표
Naver Maps api를 이용하여 프로젝트에 지도 기능을 구현한다.

## 1. 지도 API

### 1.1 Application Programming Interface
웹 서비스에서 사용할 수 있도록, 외부에서 끌어다 쓰고 싶은 기능을 제어할 수 있는 연결 수단
***
### 1.2 MAP API 활용
- 경로 찾기
- 위치 검색
- 특정 지점의 위치 명시
***
### 1.3 네이버 클라우드 플랫폼
1. https://www.ncloud.com/ 로 이동하여 회원가입, 결제수단 등록
2. 서비스 > Maps > 이용신청하기
3. 하단 Application 등록 클릭, 이용약관 동의
4. Application이름 설정
5. Service 선택 
	- Maps > Web Dynamic Map 선택
6. 서비스 환경 등록
	- Web 서비스 URL 등록 > 등록
7. 서비스 환경 등록이 완료된 Applicaion 페이지
	- 인증정보 에서 클라이언트ID와 시크릿 키 확인할 수 있다.
	- 서비스 구분을 클릭하면 설명서 페이지로 이동한다.
8. Maps > Web Dynamic Map
	- Web Dynamic Map v3 사이트 바로가기 > 클릭
***
### 1.4 Naver Maps 사이트
1. 시작하기 > 
2. Hello, World 하단의 코드를 복사하여 home.html 에 붙여넣기
***
### 1.5 Naver Maps API 예제 코드

<code>App/templates/home.html</code>
```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0, user-scalable=no">
<title>간단한 지도 표시하기</title>
<script type="text/javascript" src="https://openapi.map.naver.com/openapi/v3/maps.js?ncpClientId=YOUR_CLIENT_ID"></script>
</head>
<body>
<div id="map" style="width:100%;height:400px;"></div>
<script>
var mapOptions = {
	center: new naver.maps.LatLng(37.3595704, 127.105399),
	zoom: 10
};
var map = new naver.maps.Map('map', mapOptions);
</script>
</body>
</html>
```
***
### 1.6 Naver Maps API 예제 코드 구성

<code>App/templates/home.html</code>

- Head 의 다음 부분에 발급 받은 클라이언트 ID를 입력한다.
```html
<script type="text/javascript" src="https://openapi.map.naver.com/openapi/v3/maps.js?ncpClientId=YOUR_CLIENT_ID"></script><!—클라이언트 ID-->
```

- Body의 map div style을 수정하여 지도의 크기를 조정할 수 있다.
```html
<div id="map" style="width:50%;height:400px;"></div>

```
- Script부분을 수정하여 지도 기능과 관련된 조작이 가능하다.
```html
<script>
var mapOptions = {
	center: new naver.maps.LatLng(37.3595704, 127.105399),
	zoom: 12
};
var map = new naver.maps.Map('map', mapOptions);
</script>
```
***
### 1.7 지도 추가 생성

<code>App/templates/home.html</code>

- 기존의 코드를 복사하여 변수 명을 변경하여 사용할 수 있음
```html
<!--기존 map 하단에 map 2생성-->
<div id="map2" style="width:50%;height:400px;"></div>
<script>
var mapOptions2 = {
	center: new naver.maps.LatLng(37.3595704, 127.105399),
	zoom: 12
};
var map2 = new naver.maps.Map('map2', mapOptions2);
</script>
```
***
### 1.8 지도 위치 지정
- Scirpt 코드의 위도와 경도를 수정하여 위치를 지정할 수 있다.
- 위도 경도 얻기
1. Google Maps 에 원하는 지역의 주소를 검색
2. 검색결과 Google Maps 의 domain에서 위도와 경도를 얻을 수 있다.
	Ex) 삼육대학교
	<code>https://www.google.co.kr/maps/place/%EC%82%BC%EC%9C%A1%EB%8C%80%ED%95%99%EA%B5%90+%E4%B8%89%E8%82%B2%E5%A4%A7%E5%AD%B8%E6%A0%A1+Sahmyook+University/@37.6430449,127.1052021,18z/data=!4m5!3m4!1s0x357cb9c0cfc01725:0xbc3bb7fc0f140eac!8m2!3d37.6429515!4d127.1054757</code>
	
<code>App/templates/home.html</code>
```html
<!--Google Maps에서 얻어온 삼육대학교의 위도 경도--> 
var mapOptions2 = {
	center: new naver.maps.LatLng(37.6430449, 127.1052021),
	zoom: 13
};
```
***
### 1.9 예제 활용

https://navermaps.github.io 
- 네비 바 Examples > 예제 모아보기 에서 다양한 예제를 볼 수 있다.
- 마커, 정보 창 추가하기
	- 정보 창 표시하기 페이지로 이동하여 해당 코드를 복사하여 App/templates/home.html에 붙여 넣기
	- Scirpt 부분의 수정하여 세부 설정을 변경할 수 있다.
	- 복사 붙여넣기 만으로 작동하지 않는 예제가 있을 수 있다.
