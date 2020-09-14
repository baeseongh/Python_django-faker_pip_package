from django.db import models
from imagekit.models import ImageSpecField #썸네일 생성
from imagekit.processors import ResizeToFill #썸네일 크기조정

class Blog(models.Model):
    text = models.TextField()

class Pictures(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to="blogimg")
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(150, 150)], format='JPEG', options= {'quality':60}) #썸네일 이미지 지정, 크기지정(크기), 확장자, 압충 방식 
