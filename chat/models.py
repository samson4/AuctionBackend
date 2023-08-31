from django.db import models


from Users.models import User
# Create your models here.
class Message(models.Model):
    body = models.TextField()
    sent_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,blank=True,null=True,on_delete=models.SET_NULL)

    def __str__(self) :
        return self.sent_by
    

class Room(models.Model):
    WAITING = 'waiting'
    ACTIVE = 'active'
    CLOSED= 'closed'

    STATUS_CHOISE = (
    (WAITING ,'waiting'),
    (ACTIVE ,'active'),
    (CLOSED,'closed'),
    )
    uuid = models.CharField(max_length=255)
    client = models.CharField(max_length=255)
    agent = models.ForeignKey(User,related_name='rooms',blank=True,null=True,on_delete=models.SET_NULL)
    Message = models.ManyToManyField(Message,blank=True)
    url = models.CharField(max_length=255,blank=True,null=True)
    status = models.CharField(max_length=25,choices=STATUS_CHOISE,default=WAITING)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.client} - {self.uuid}'
    

