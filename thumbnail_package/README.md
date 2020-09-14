# Django Imagekit Thumbnail 구현

## 학습 목표
Imagekit pip 패키지를 사용하여 Thumbnail 기능을 구현한다.
	
## 1. Thumbnail

### 1.1 Thumbnail pip 패키지를 사용하는 이유

1. 썸네일 파일 지정 용이
2. 파일 용량 관리 용이
	- 확장자, 압축방식 지정가능, 중복 사용 방지
3. 파일 분류에 효율적
	- 썸네일 파일과 본 파일을 효율적으로 관리할 수 있다.
***
### 1.2 Thumbnail 실습 기본 세팅

#### 1.2.1 모델 정의

<code>App/models.py</code>
```python
class Pictures(models.Model):
	text = models.TextField()
	image = models.ImageField(upload_to="blogimg")
```


#### 1.2.2 미디어 파일 정의

<code>Project/settings.py</code>
```python
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

#### 1.2.3 URL 세팅

Settings, Static 임포트, urlpatterns에 static 함수 더하기

<code>project/urls.py</code>
```python
class Pictures(models.Model):
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', views.home, name="home"),
	path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

#### 1.2.4 Admin 세팅

<code>app/admin.py</code>
```python
from django.contrib import admin
from .models import Pictures

admin.site.register(Pictures)
```

#### 1.2.5 Views 세팅

<code>App/views.py</code>
```python
from .models import Pictures
#모델 임포트, 오프젝트 가져오기
def home(request):
	blog = Pictures.objects
	return render(request, 'home.html', {'blog':blog})
```

#### 1.2.6 template 세팅

<code>app/templates/home.html</code>
```python
from .models import Pictures
#모델 임포트, 오프젝트 가져오기
{%for blog in blog.all%}
<img src="{{blog.image.url}}" width = 500>
<br>
<p>{{blog.text}}</p>
<br>
{%endfor%}
```
모델 마이그레이트
***
### 1.3 Pip 패키지 설치

#### 1.3.1 django-imagekit
```shall
$ pip install pillow django-imagekit
```

#### 1.3.2 Image kit 등록

<code>Project/settings.py</code>
```python
INSTALLED_APPS = [
'imagekit',
] 
```
***
### 1.4 썸네일 모델 등록

<code>App/models.py</code>
#### 1.4.1 임포트와 변수 생성
```python
INSTALLED_APPS = [
from imagekit.models import ImageSpecField #썸네일 생성
from imagekit.processors import ResizeToFill #썸네일 크기조정
class Pictures(models.Model):
	text = models.TextField()
I	mage = models.ImageField(upload_to="blogimg")
	image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(120, 60)]) #썸네일 이미지 지정, 크기지정(가로, 세로)
] 
```
***
### 1.5 템플릿에 썸네일 표출

<code>App/templates/home.html</code>
```python
<img src="{{blog.image_thumbnail.url}}" alt="thumbnail image">
```
***
### 1.6 ImageSpecField 인자 속성

<code>App/models.py</code>
```python
image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(150, 150)], format='JPEG', options= {'quality':60}) #썸네일 이미지 지정, 크기지정(크기), 확장자, 압축방식 =

```
