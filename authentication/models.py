from django.db import models


# Create your models here.
# class User(models.Model):
#     username = models.CharField(max_length=255)
#     password = models.CharField(max_length=255)
#     email = models.EmailField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.username


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
