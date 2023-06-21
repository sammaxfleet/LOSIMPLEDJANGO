from django.db import models
from django.contrib.auth.models import User
import os
from uuid import uuid4
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.


def path_and_rename(instance, filename):
    upload_to = 'images/user_profile/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to=path_and_rename, default='images/account.png')
    # friends = models.ManyToManyField('UserProfile', related_name = "my_friends")

    def __str__(self):
        return self.user.username

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        if os.path.exists(self.image.url):
            os.remove(self.image.path)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


# class Friend(models.Model):
#     profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.profile.user.username
