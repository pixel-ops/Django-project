from django.db import models
from datetime import datetime
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
    
# Create your models here.

class mycontact(models.Model):
    
    name = models.CharField(max_length=122)
    password = models.CharField(max_length=122)
    address1 = models.TextField()
    address2 = models.TextField()
    city = models.CharField(max_length=122)
    state = models.CharField(max_length=122)
    zip = models.CharField(max_length=122)

    def __str__(self) -> str:
        return self.name
    
class myabout(models.Model):

    userid = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=122, blank=False, null=False)
    last_name = models.CharField(max_length=122, blank=False, null=False)
    phone = models.CharField(max_length=122)
    email = models.EmailField()
    address = models.TextField()
    extra = models.ForeignKey(mycontact, on_delete=models.CASCADE,null=True)

    def __str__(self) -> str:
        return self.first_name + ' ' +self.last_name

  
class myregister(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField()
    user_password = models.CharField(max_length=122)
    user_location = models.CharField(max_length=122)
    user_number = models.IntegerField(null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.user_name


class mypost(models.Model):

    userid = models.AutoField(primary_key=True)
    topic = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    time = models.TimeField(default=timezone.now)
    date = models.DateField(default=datetime.today)
    # content = models.TextField()
    content = RichTextField(blank=True, null=True)
    content_type = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    img = models.ImageField(upload_to='img', blank=True)

    def __str__(self) -> str:
        return self.author

    
class multiple_images(models.Model):
    post = models.ForeignKey(mypost, default=None, on_delete=models.CASCADE)
    image = models.FileField(upload_to='myimg')
