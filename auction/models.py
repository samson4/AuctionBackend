from django.db import models
import uuid
from Users.models import User
# Create your models here.

class Auction(models.Model):
    STATUS = [
        ('ACTIVE','Active'),
        ('PREPARING','Preparing'),
    ]
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = models.CharField(max_length=100,blank=False,default='')
    status = models.CharField(choices=STATUS,max_length=50,default='PREPARING')
    subscribers = models.ManyToManyField(User,blank=True,default=None)
    
    
    def __str__(self):
        return self.title

class Lot(models.Model):
    CONDITION = [

          ('USEABLE','Useable'),
          ('USED','Used'),
          ('SCRAP','Scrap'),
          ('RERAIRABLE','Repairable'),
     ]
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False) 
    auction = models.ForeignKey(Auction,null=True,blank=True,on_delete=models.SET_NULL) 
    title = models.CharField(max_length=100,blank=False,default='')
    description = models.TextField(max_length=500) 
    condition = models.CharField(choices=CONDITION,max_length=100)
    # image = models.ImageField()
    Price = models.FloatField()

    def lot_count(self):
        return Lot.objects.count()

    def __str__(self):
        return self.title
    
    def __repr__(self):
        return 'Lot %s' %self.title 





