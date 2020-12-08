from django.db import models
from django.urls import reverse
# Create your models here.
class User(models.Model):
        name=models.TextField(max_length=50)
        password=models.TextField(max_length=50)
        id = models.TextField(max_length=50),


class comment(models.Model):
    id=models.TextField(max_length=50),
    work=models.TextField(max_length=100)
    username=models.TextField(max_length=50)
    date_posted=models.DateField(auto_now_add=True)
    comment=models.TextField(blank=True)
    Age=models.IntegerField()
    name=models.TextField(max_length=50)
    def getworktitle(self):
        thiswork=work.objects.get(title=self.work)
        return thiswork.title
    def get_absolute_url(self):
        thiswork=work.objects.get(title=self.work)
        return reverse('enzyme:enzyme_offic_listdetail',args=[thiswork.id])

class work(models.Model):
    id=models.TextField(max_length=50),
    title=models.TextField(max_length=100)
    url=models.TextField(max_length=100)
    imgposition=models.TextField(max_length=100)
    author=models.TextField(max_length=100)
    createdate=models.DateField(auto_now_add=True)
    description=models.TextField(max_length=100)
    country=models.TextField(max_length=100)




