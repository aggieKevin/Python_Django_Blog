from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from PIL import Image

# Create your models here.
class Profile(models.Model): 
    user=models.OneToOneField(User,on_delete=models.CASCADE) # can use user.profile 
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return self.user.username + ' Profile'
    def save(self):
        super().save()
        img=Image.open(self.image.path)
        if img.height >300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


def create_profile(sender,**kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])

def save_profile(sender,**kwargs):
    kwargs['instance'].profile.save()

post_save.connect(create_profile,sender=User)
post_save.connect(save_profile,sender=User)
