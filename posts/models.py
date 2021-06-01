from django.db import models
#from datetime import timedelta
from django.utils import timezone

class Post(models.Model):
    author = models.CharField('작성자 / Writer',max_length= 20,blank=True)
    contents = models.TextField('내용 / Contents',max_length=1000,blank=True)
    id = models.AutoField

    def __str__(self):
        return self.contents

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField('작성자',max_length= 20,blank=True)
    created_date = models.DateField('Date',max_length=10,default=timezone.now,blank=True)
    text = models.TextField('Comments',max_length=1000,blank=True)

    def __str__(self):
        return self.created_date

