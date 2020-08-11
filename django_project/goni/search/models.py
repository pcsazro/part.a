from django.db import models

# Create your models here.
from django.db import models


# Create your models here.


class Place(models.Model):
    contentid = models.CharField(max_length=50, primary_key=True)
    contenttypeid = models.CharField(max_length=20)
    areacode = models.CharField(max_length=20)
    sigungucode = models.CharField(max_length=20)
    place_title = models.CharField(max_length=100, blank=True, default='')
    mapx = models.CharField(max_length=100)
    mapy = models.CharField(max_length=100)
    firstimage = models.CharField(max_length=500, blank=True, default='')
    overview = models.TextField(null=False)
    addr = models.CharField(max_length=500)
    tel = models.CharField(max_length=50, null=False, default='')
    homepage = models.CharField(max_length=500, null=False)

    def __str__(self):
        return 'id %s' % (self.contentid)
        # return '장소 이름 : %s, 주소 : %s' %(self.place_title, self.place_id)


class Mark(models.Model):
    m_id = models.CharField(max_length=100)
    # contentid = models.ForeignKey(Place, on_delete=models.CASCADE)
    place_id = models.CharField(max_length=100)
    mark_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-mark_date']

    def __str__(self):
        return '찜 member: %s, place : %s, date : %s' % (self.m_id, self.place_id, self.mark_date)


# 순위차트용 Table
class RankWord(models.Model):
    word = models.CharField(max_length=500)
    count = models.IntegerField(default=0)
    sd_date = models.DateField()