from tkinter import Image
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=650)
    phone = models.IntegerField(null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pic')

    def __str__(self) -> str:
        return f"{self.user.username}-Profile"

    # def save(self, *args, **kwargs):
    #     super().save(*args,**kwargs)
    #     img = Image.open(self.image.path)
    #     if img.height>300 or img.width>300:
    #         output_size = (300,300)
    #         img.save(self.image.path)