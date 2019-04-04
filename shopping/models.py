from django.db import models

# Create your models here.

class 商品类别表(models.Model):
    名称 = models.CharField(max_length = 50, unique = True)
    描述 = models.TextField(blank = True)
    图片 = models.ImageField(upload_to = 'category',blank = True)
    class Meta:
        verbose_name_plural = "商品类别表"
        db_table = "商品类别表"
    def __str__(self):
        return self.名称

class 产品列表(models.Model):
    名称 = models.CharField(max_length = 100, unique = True)
    描述 = models.TextField(blank = True)
    图片 = models.ImageField(upload_to = 'category',blank = True)
    所属类别 = models.ForeignKey(商品类别表, on_delete = models.CASCADE)
    价格 = models.DecimalField(max_digits = 10,decimal_places = 2)
    库存 = models.IntegerField(default = 0)
    已上架 = models.BooleanField(default = True)
    创建时间 = models.DateTimeField(auto_now_add = True)
    修改时间 = models.DateTimeField(auto_now_add = True)
    class Meta:
        verbose_name_plural = "产品列表"
        db_table = '产品列表'
        ordering = ('-创建时间',)
    def __str__(self):
        return self.名称