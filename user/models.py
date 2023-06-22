from django.db import models

# Create your models here.
import os
from django.contrib.auth.models import User
from django.db import models
from uuid import uuid4


def user_profile_image_upload_to(instance, filename):
    # Get the file extension
    ext = filename.split('.')[-1]
    # Generate a unique identifier
    unique_id = str(uuid4())
    # Create the new filename using the username and unique identifier
    new_filename = f"{instance.user.username}_{unique_id}.{ext}"
    # Return the complete upload path
    return os.path.join("profile_images", new_filename)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(
        upload_to=user_profile_image_upload_to, blank=True, null=True)

   # def __str__(self):
    # return self.user.username
