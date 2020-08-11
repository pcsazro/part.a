from django.db import models
from django.urls import reverse


class Member(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    pw = models.CharField(max_length=100, )
    name = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=80)

    def __str__(self):
        return '아이디:' + self.id + 'pw: ' + self.pw + 'name: ' + self.name + 'tel: ' + self.tel + 'email: ' + self.email + '성별' + self.gender

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])
