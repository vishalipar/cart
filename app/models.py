from django.db import models

# Create your models here.


class Banners(models.Model):
    images = models.ImageField(upload_to='photos/banners')
    
    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'
    
    def __int__(self):
        return self.id
    
class SmallBanners(models.Model):
    smallimages = models.ImageField(upload_to='photos/smallbanners', null=True)
    
    class Meta:
        verbose_name = 'SmallBanner'
        verbose_name_plural = 'SmallBanners'
    
    def __int__(self):
        return self.id
    