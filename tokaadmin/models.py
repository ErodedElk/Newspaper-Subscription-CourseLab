from operator import truediv
from django.db import models
from django.utils.safestring import mark_safe



class newspaper(models.Model):
    ssid=models.IntegerField(max_length=10,verbose_name="刊号",blank=True,default=None)
    paper_name=models.CharField(verbose_name="刊名",max_length=10,blank=True,default=None)
    #paper_name=models.ForeignKey(to=newspapername, on_delete=models.CASCADE, related_name='刊名', verbose_name='刊名')
    phone_number=models.IntegerField(verbose_name="订阅号码",blank=True,default=None)
    productor=models.CharField(verbose_name="出版社",max_length=8,blank=True,default=None)

    def __str__(self):
        return str(self.paper_name)
    def __unicode__(self):
        return str(self.paper_name)
    class Meta:
        verbose_name = '可订阅刊物'
        verbose_name_plural = verbose_name
        ordering = ['ssid', 'paper_name']

    def check_data(self, temp_ssid_id):
        order_exists = newspaper.objects.filter(ssid=temp_ssid_id,)
        if order_exists.exists():
            return order_exists[0]
        else:
            return False
    def save(self):
        temp_ssid_id = self.ssid
        order_exists = newspaper.objects.filter(ssid=temp_ssid_id, )
        if order_exists.exists():
            self.id = order_exists.last().id
        else:
            pass
        super().save()



class Subscriber(models.Model):
    phone_n=models.IntegerField(max_length=11,verbose_name="手机号",blank=True,default=None)
    sub_name=models.CharField(verbose_name="姓名",max_length=4,blank=True,default=None)
    sub_address=models.CharField(verbose_name="住址",max_length=20,blank=True,default=None)
    sub_target=models.ManyToManyField(newspaper,blank=True,default=None,related_name="刊名",verbose_name="刊名")

    
    def get_target(self):
        return (','.join([str(i.paper_name) for i in self.sub_target.all()]))
    testdata=property(get_target)


    def __str__(self):
            return self.sub_name

    class Meta:
        verbose_name = '订阅者'
        verbose_name_plural = verbose_name
        ordering = ['phone_n', 'sub_name']
