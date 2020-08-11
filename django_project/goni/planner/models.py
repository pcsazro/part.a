from django.db import models
from search.models import Place

# Create your models here.
class PlannerM(models.Model):
    p_title = models.CharField(max_length=200)  # 플래너 이름
    m_id = models.CharField(max_length=100)  # 작성자 아이디
    open_flag = models.CharField(max_length=100)  # 공개여부
    t_start = models.CharField(max_length=100)  # 여행시작일
    t_end = models.CharField(max_length=100)  # 여행종료일
    concept = models.CharField(max_length=100)  # 여행컨셉

    def __str__(self):
        return '%d' % self.id


# class Place(models.Model):
#     contentid = models.CharField(max_length=50, primary_key=True)  # 여행지아이디
#     contenttypeid = models.CharField(max_length=20)  # 여행지 타입
#     areacode = models.CharField(max_length=20)  # 지역코드
#     sigungucode = models.CharField(max_length=20)  # 시군구코드
#     place_title = models.CharField(max_length=100, blank=True, default='')  # 여행지이름
#     mapx = models.CharField(max_length=100)  # 경도
#     mapy = models.CharField(max_length=100)  # 위도
#     firstimage = models.CharField(max_length=500, blank=True, default='')  # 대표이미지
#     overview = models.TextField(default='')  # 상세설명
#     addr = models.TextField()  # 주소
#     tel = models.CharField(max_length=50, blank=True, default='')  # 전화번호
#     homepage = models.CharField(max_length=500, blank=True, default='')  # 홈페이지
#
#     def __str__(self):
#         return '여행지 번호: %s, 여행지 이름: %s' % (self.contentid, self.place_title)


class PlannerD(models.Model):
    p_id = models.ForeignKey(PlannerM, on_delete=models.CASCADE)  # 플래너아이디
    seq = models.IntegerField()  # 순서
    contentid = models.ForeignKey(Place, on_delete=models.CASCADE)  # 여행지id

    def __str__(self):
        return '플래너 번호: %s, 여행지 번호: %s, 순서: %d' % (self.p_id, self.contentid, self.seq)
